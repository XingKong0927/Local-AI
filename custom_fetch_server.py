"""无用！"""

#!/usr/bin/env python3
import sys
import json
import requests
from typing import Dict, Any, List

class SimpleFetchServer:
    def __init__(self):
        self.methods = {
            "initialize": self.initialize,
            "tools/list": self.list_tools,
            "tools/call": self.call_tool,
        }
    
    def initialize(self, params: Dict) -> Dict:
        return {
            "protocolVersion": "2024-11-05",
            "capabilities": {
                "tools": {"listChanged": False}
            },
            "serverInfo": {
                "name": "custom-fetch",
                "version": "1.0.0"
            }
        }
    
    def list_tools(self, params: Dict) -> Dict:
        return {
            "tools": [
                {
                    "name": "fetch",
                    "description": "Fetch content from a URL with custom User-Agent",
                    "inputSchema": {
                        "type": "object",
                        "properties": {
                            "url": {"type": "string", "description": "The URL to fetch"},
                            "max_length": {
                                "type": "integer", 
                                "description": "Maximum length of the returned content",
                                "default": 5000
                            }
                        },
                        "required": ["url"]
                    }
                }
            ]
        }
    
    def call_tool(self, params: Dict) -> Dict:
        name = params.get("name", "")
        arguments = params.get("arguments", {})
        
        if name == "fetch":
            url = arguments.get("url", "")
            max_length = arguments.get("max_length", 5000)
            
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                # "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat",
            }
            
            try:
                response = requests.get(url, headers=headers, timeout=30)
                response.raise_for_status()
                content = response.text[:max_length]
                
                return {
                    "content": [
                        {"type": "text", "text": content}
                    ]
                }
            except Exception as e:
                return {
                    "content": [
                        {"type": "text", "text": f"Error: {str(e)}"}
                    ],
                    "isError": True
                }
        
        return {
            "content": [
                {"type": "text", "text": f"Unknown tool: {name}"}
            ],
            "isError": True
        }
    
    def handle_request(self, request: Dict) -> Dict:
        method = request.get("method", "")
        if method in self.methods:
            result = self.methods[method](request.get("params", {}))
            return {
                "jsonrpc": "2.0",
                "id": request.get("id"),
                "result": result
            }
        
        return {
            "jsonrpc": "2.0",
            "id": request.get("id"),
            "error": {
                "code": -32601,
                "message": f"Method not found: {method}"
            }
        }
    
    def run(self):
        """运行服务器主循环"""
        while True:
            try:
                line = sys.stdin.readline()
                if not line:
                    break
                
                request = json.loads(line.strip())
                response = self.handle_request(request)
                print(json.dumps(response))
                sys.stdout.flush()
                
            except Exception as e:
                error_response = {
                    "jsonrpc": "2.0",
                    "id": None,
                    "error": {
                        "code": -32700,
                        "message": f"Parse error: {str(e)}"
                    }
                }
                print(json.dumps(error_response))
                sys.stdout.flush()

if __name__ == "__main__":
    # 安装 requests 如果尚未安装
    try:
        import requests
    except ImportError:
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
        import requests
    
    server = SimpleFetchServer()
    server.run()

