# ベースイメージは Ubuntu 最新
FROM ubuntu:22.04

# 必要パッケージ
RUN apt-get update && apt-get install -y \
    texlive-lang-cjk \
    texlive-latex-extra \
    latexmk \
    dvipng \
    fonts-ipafont-gothic \
    fonts-ipafont-mincho \
    rclone \
    curl \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ
WORKDIR /workspace