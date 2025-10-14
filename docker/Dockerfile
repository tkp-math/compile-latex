# ベースイメージ
FROM ubuntu:22.04

# タイムゾーン設定を非対話化
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Tokyo

# 必要パッケージのインストール
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        tzdata \
        texlive-lang-cjk \
        texlive-latex-extra \
        latexmk \
        dvipng \
        fonts-ipafont-gothic \
        fonts-ipafont-mincho \
        rclone \
        git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリ
WORKDIR /workspace
