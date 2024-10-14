FROM python:3.9-slim

# Установка необходимые зависимости
RUN apt-get update && \
    apt-get install -y \
    wget \
    unzip \
    gnupg2 \
    libnss3-dev \
    libxss1 \
    libgconf-2-4 \
    libxi6 \
    libxrender1 \
    libgtk-3-0 \
    && rm -rf /var/lib/apt/lists/*

# Установка Google Chrome
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/google.gpg && \
    echo "deb [signed-by=/usr/share/keyrings/google.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list && \
    apt-get update && apt-get install -y google-chrome-stable && \
    rm -rf /var/lib/apt/lists/*

# Установка Python-библиотеки
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /app
COPY . .
CMD ["pytest", "tests", "--alluredir=allure-results"]