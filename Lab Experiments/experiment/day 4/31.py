
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs
import html

# Store blog posts
posts = []

class BlogServer(BaseHTTPRequestHandler):

    def do_GET(self):
        self.show_page()

    def do_POST(self):
        length = int(self.headers.get('Content-Length', 0))
        data = self.rfile.read(length).decode('utf-8')

        form = parse_qs(data)

        title = form.get('title', [''])[0].strip()
        content = form.get('content', [''])[0].strip()

        if title and content:
            posts.append({
                'title': title,
                'content': content
            })

        self.send_response(303)
        self.send_header('Location', '/')
        self.end_headers()

    def show_page(self):

        page = """
        <!DOCTYPE html>
        <html>
        <head>
        <title>My Web Blog</title>

        <style>
        body {
            font-family: Arial;
            background: #eaf2f8;
            padding: 30px;
        }

        .container {
            background: white;
            padding: 25px;
            max-width: 600px;
            margin: auto;
            border-radius: 10px;
        }

        h1 {
            text-align: center;
            color: blue;
        }

        input, textarea {
            width: 95%;
            padding: 10px;
            margin: 10px 0;
        }

        button {
            background: blue;
            color: white;
            padding: 12px;
            border: none;
            cursor: pointer;
        }

        .post {
            background: #dceeff;
            padding: 15px;
            margin-top: 15px;
        }
        </style>

        </head>

        <body>
        <div class="container">

        <h1>MY WEB BLOG</h1>

        <h2>Create New Blog</h2>

        <form method="POST">

        <input type="text" name="title"
        placeholder="Enter Blog Title" required>

        <textarea name="content"
        placeholder="Write Your Blog"
        required></textarea>

        <button type="submit">Publish Blog</button>

        </form>

        <h2>Published Blogs</h2>
        """

        for post in posts:
            page += f"""
            <div class="post">
            <h3>{html.escape(post['title'])}</h3>
            <p>{html.escape(post['content'])}</p>
            </div>
            """

        page += """
        </div>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()

        self.wfile.write(page.encode('utf-8'))


# Start web server
server = HTTPServer(('127.0.0.1', 8000), BlogServer)

print("Web Blog Server Started Successfully!")
print("Open browser: http://127.0.0.1:8000")

server.serve_forever()
