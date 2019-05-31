from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import tacticalmap.routing

#channels根路由配置文件
#导入 AuthMiddlewareStack、URLRouter 和 chat.routing ;并在 ProtocolTypeRouter 列表中插入一个 "websocket" 键, 格式如下:
# 这个根路由配置指定，当与 Channels 开发服务器建立连接的时候, ProtocolTypeRouter 将首先检查连接的类型。如果是 WebSocket 连接 (ws://或 wss://), 则连接会交给 AuthMiddlewareStack。
application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            tacticalmap.routing.websocket_urlpatterns
        )
    ),
})