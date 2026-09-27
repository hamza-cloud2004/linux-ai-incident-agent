import os
import requests
from flask import Flask, request, jsonify

# --- OpenTelemetry Tracing Setup ---
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.flask import FlaskInstrumentor

provider = TracerProvider()
processor = BatchSpanProcessor(OTLPSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(provider)

app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)

tracer = trace.get_tracer(__name__)

# Ollama local server ka address. Docker-compose network mein service ka
# naam 'ollama' hoga, isliye localhost ki bajaye 'ollama' likha hai.
OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://ollama:11434")
MODEL_NAME = os.environ.get("OLLAMA_MODEL", "llama3.2:1b")

SYSTEM_INSTRUCTION = (
    "Your name is Linux AI. You are an expert Linux SRE (Site Reliability Engineering) AI Agent. "
    "Your user is Hamza. Your core focus is on reliability, scalability, analyzing system logs and metrics, "
    "identifying Root Cause Analysis (RCA), and fixing system issues. Always introduce yourself as Linux AI "
    "when asked for your name, and address your user as Hamza, offering your specialized assistance."
)


def call_ai_agent(user_prompt: str) -> str:
    with tracer.start_as_current_span("ai_agent_call"):
        response = requests.post(
            f"{OLLAMA_HOST}/api/chat",
            json={
                "model": MODEL_NAME,
                "messages": [
                    {"role": "system", "content": SYSTEM_INSTRUCTION},
                    {"role": "user", "content": user_prompt}
                ],
                "stream": False
            },
            timeout=120
        )
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "Flask SRE Agent with local Ollama model is running!"
    }), 200


@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        if not data or "prompt" not in data:
            return jsonify({"error": "Missing 'prompt' in request body"}), 400

        user_prompt = data["prompt"]
        agent_reply = call_ai_agent(user_prompt)

        return jsonify({
            "status": "success",
            "agent_response": agent_reply
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "agent_error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
