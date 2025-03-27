# Simple HTML Web Server with Hidden File List

This project creates a lightweight Python web server that serves multiple HTML files. The first page (`1.html`) is the default page, and it includes a **hidden** list of all available HTML files inside an HTML comment (`<!-- ... -->`). Users can view this list only through "Inspect Element" in their browser.

## Features

- Serves static HTML files using Python's `http.server`.
- `1.html` is the default landing page.
- Injects a **hidden** (commented-out) list of available `.html` files.
- Designed to be run inside a Docker container.

---

## Project Structure

```
├── Dockerfile
├── server.py
├── public/
│   ├── 1.html  (Default Page)
│   ├── 2.html
│   ├── 3.html
│   ├── ...
│   ├── index.html (Optional)
```

---

## Getting Started

### 1️⃣ Build the Docker Image

```sh
docker build --no-cache -t my-webserver .
```

### 2️⃣ Run the Container

```sh
docker run -d -p 8080:80 --name my-container my-webserver
```

This will start the server on port **8080**.

### 3️⃣ Access the Webpage

- Open your browser and visit [**http://localhost:8080/**](http://localhost:8080/)
- It will show the contents of `1.html`.

### 4️⃣ Inspect Element to See Hidden Files

- Right-click on the page → **Inspect** → **Elements**
- Look for an HTML comment like this:

```html
<!--
<ul>
  <li>1.html</li>
  <li>2.html</li>
  <li>3.html</li>
</ul>
-->
```

---

## How It Works

### `server.py`

- Redirects `/` to `1.html`.
- Finds all `.html` files in the directory and sorts them numerically.
- Injects a hidden file list inside `1.html` (inside `<!-- ... -->`).
- Runs on Python's built-in `http.server`.

---

## Stopping the Container

To stop and remove the running container:

```sh
docker stop my-container && docker rm my-container
```

---

## Notes

- Only files with numeric names (`1.html`, `2.html`, etc.) are included in the hidden list.
- `index.html` (if present) is ignored to prevent errors.
---

