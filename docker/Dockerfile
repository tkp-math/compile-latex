# ベースは Ubuntu
FROM ubuntu:22.04

# 環境変数
ENV DEBIAN_FRONTEND=noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8

# 必要パッケージのインストール
RUN apt-get update && apt-get install -y \
    texlive-full \
    texlive-lang-japanese \
    latexmk \
    dvipdfmx \
    fonts-ipafont \
    fonts-ipaexfont \
    python3 \
    python3-pip \
    curl \
    unzip \
    git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Python追加
RUN apt-get update && apt-get install -y python3 python3-pip

# python コマンドを python3 にリンク
RUN update-alternatives --install /usr/bin/python python /usr/bin/python3 1

# pip コマンドを pip3 にリンク
RUN update-alternatives --install /usr/bin/pip pip /usr/bin/pip3 1

# 作業ディレクトリ
WORKDIR /workspace

# デフォルトで bash を使う
CMD ["bash"]
