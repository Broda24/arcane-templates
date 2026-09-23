# Ollama

## English

Local model runner using the official Docker Hub image. The unauthenticated API is bound to localhost by default; do not expose it publicly. Download models from the container console (for example, `ollama pull gemma3`). Model files persist in `ollama-models`. GPU acceleration is not configured and requires host-specific device settings.

Sources: [Ollama](https://ollama.com/), [official Docker image](https://hub.docker.com/r/ollama/ollama).

## Deutsch

Lokale Laufzeit für Sprachmodelle mit dem offiziellen Docker-Hub-Image. Die API ohne Anmeldung ist standardmäßig nur an localhost gebunden; nicht öffentlich freigeben. Modelle über die Container-Konsole herunterladen (z. B. `ollama pull gemma3`). Modelldateien bleiben im Volume `ollama-models`. GPU-Beschleunigung ist nicht vorkonfiguriert und benötigt host-spezifische Gerätefreigaben.

Quellen: [Ollama](https://ollama.com/), [offizielles Docker-Image](https://hub.docker.com/r/ollama/ollama).
