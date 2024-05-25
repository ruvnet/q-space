# Use a minimal base image
FROM mcr.microsoft.com/devcontainers/base:ubuntu-22.04

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && apt-get install -y \
    curl \
    git \
    build-essential \
    python3-pip \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Install Azure CLI
RUN curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Install Python packages
RUN pip3 install azure-quantum qsharp

# Set the working directory
WORKDIR /workspace

# Copy the project files
COPY . /workspace

# Set the entrypoint
ENTRYPOINT ["/bin/bash"]

# Expose necessary ports
EXPOSE 8080

# Add a health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -f http://localhost:8080 || exit 1

# Clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Use a non-root user
RUN useradd -ms /bin/bash devuser
USER devuser

# Label the image
LABEL maintainer="Your Name <your.email@example.com>"
LABEL description="Optimized Dockerfile for GitHub Codespaces"
LABEL version="1.0"
