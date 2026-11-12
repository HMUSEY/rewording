#!/usr/bin/env python3
import json
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

LOG_PATH = sys.argv[2] if len(sys.argv) > 2 else None


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        return

    def _send(self, status, payload, extra=None):
        data = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(data)))
        for key, value in (extra or {}).items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(data)

    def do_POST(self):
        length = int(self.headers.get("content-length", "0"))
        raw = self.rfile.read(length)
        try:
            body = json.loads(raw)
        except ValueError:
            body = None
        if LOG_PATH:
            with open(LOG_PATH, "a", encoding="utf-8") as handle:
                handle.write(
                    json.dumps(
                        {
                            "path": self.path,
                            "headers": {k.lower(): v for k, v in self.headers.items()},
                            "body": body,
                        }
                    )
                    + "\n"
                )
        if self.headers.get("x-api-key", "").startswith("sk-ant-redirect"):
            self._send(302, {}, {"location": "http://127.0.0.1:1/steal"})
            return
        if self.headers.get("x-api-key", "").startswith("sk-ant-denied"):
            self._send(401, {"type": "error", "error": {"type": "authentication_error", "message": "invalid x-api-key"}})
            return
        if self.path == "/v1/messages/count_tokens":
            self._send(200, {"input_tokens": 1234})
        elif self.path == "/v1/messages":
            self._send(
                200,
                {
                    "content": [{"type": "thinking", "thinking": "", "signature": "x"}, {"type": "text", "text": "MOCK REPLY"}],
                    "stop_reason": "end_turn",
                    "usage": {
                        "input_tokens": 11,
                        "output_tokens": 22,
                        "cache_creation_input_tokens": 33,
                        "cache_read_input_tokens": 0,
                    },
                },
            )
        else:
            self._send(404, {"type": "error", "error": {"type": "not_found_error", "message": "no route"}})


if __name__ == "__main__":
    port = int(sys.argv[1])
    HTTPServer(("127.0.0.1", port), Handler).serve_forever()
