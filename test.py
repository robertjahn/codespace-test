import os

print("DT_BASE_URL = " + os.getenv("DT_BASE_URL", ""))
print("DYNATRACE_API_TOKEN = " + os.getenv("DYNATRACE_API_TOKEN", ""))
print("NVIDIA_API_KEY = " + os.getenv("NVIDIA_API_KEY", ""))
print("TAVILY_API_KEY = " + os.getenv("TAVILY_API_KEY", ""))
print("OTEL_OTLP_ENDPOINT = " + os.getenv("OTEL_OTLP_ENDPOINT", ""))
