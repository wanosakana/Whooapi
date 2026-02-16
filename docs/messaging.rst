==========
Messaging
==========

Messaging and communication endpoints.

Get Stamp Messages
==================

.. http:get:: /api/stamp_messages

   Retrieve stamp messages.

   **Request Headers:**

   .. code-block:: http

      Accept: application/json
      Authorization: Bearer <token>
      Cookie: _message_backend_session=...

   **Response:**

   :statuscode 200: Stamp messages retrieved
   :statuscode 304: Not Modified (cached)

   .. note::
      Stamp messages are pre-defined emoji or sticker messages.

Message Types
=============

The messaging system supports:

1. **Stamp Messages**: Pre-defined stickers/emojis
2. **Text Messages**: Standard text communication
3. **Location Shares**: Share current location

WebSocket Connection
====================

Real-time messaging uses WebSocket:

.. code-block:: http

   GET /cable?token=<jwt_token> HTTP/1.1
   Host: www.wh00.ooo:443
   Upgrade: websocket
   Connection: Upgrade
   Sec-WebSocket-Version: 13
   Sec-WebSocket-Key: ZGZrdmh3dmJyenZsbnhlYg==
   Origin: wss://www.wh00.ooo

   Response:
   HTTP/1.1 101 Switching Protocols
   Upgrade: websocket
   Connection: Upgrade

**Connection Parameters:**

:token: JWT authentication token (query parameter)
:protocol: WebSocket (wss://)
:port: 443 (HTTPS)

WebSocket Events
================

After connection, subscribe to channels:

.. code-block:: json

   {
     "command": "subscribe",
     "identifier": "{"channel":"MessageChannel"}"
   }

Message Format
==============

Messages are sent as JSON:

.. code-block:: json

   {
     "command": "message",
     "identifier": "{"channel":"MessageChannel"}",
     "data": {
       "action": "send_message",
       "message": "Hello!"
     }
   }

Error Handling
==============

.. warning::
   WebSocket connections may be blocked by proxies like Charles.
   Use direct connections for real-time features.

Best Practices
==============

.. tip::
   Implement reconnection logic for dropped connections.

.. tip::
   Use heartbeat/ping messages to keep connections alive.
