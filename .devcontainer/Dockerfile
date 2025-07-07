# syntax=docker/dockerfile:1

# Arguments
ARG UV_VERSION=latest
ARG DEBIAN_VERSION=bookworm

# Stage 1: Get uv binary
FROM ghcr.io/astral-sh/uv:${UV_VERSION} AS uv-binary

# Stage 2: Final image based on official VS Code devcontainer image
FROM mcr.microsoft.com/vscode/devcontainers/base:${DEBIAN_VERSION}

# Install required system packages (Python runtime is not needed separately, uv includes it)
RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy uv binary
COPY --from=uv-binary /uv /usr/local/bin/uv
COPY --from=uv-binary /uvx /usr/local/bin/uvx

# Make sure it's executable
RUN chmod +x /usr/local/bin/uv /usr/local/bin/uvx

WORKDIR /workspaces/fastapi-thirdparty-api


# Optional: create and initialize a uv project if not already present
COPY ./init-venv.sh /usr/local/bin/init-venv.sh
RUN chmod +x /usr/local/bin/init-venv.sh

# Use bash by default
CMD [ "bash" ]
