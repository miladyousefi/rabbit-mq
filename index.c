#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <amqp_tcp_socket.h>
#include <amqp.h>
#include <amqp_framing.h>

#define AMQP_BROKER_HOST ""
#define AMQP_BROKER_PORT 5672
#define AMQP_QUEUE_NAME ""

int main() {
    amqp_socket_t *socket = NULL;
    amqp_connection_state_t conn;

    conn = amqp_new_connection();

    socket = amqp_tcp_socket_new(conn);
    if (!socket) {
        fprintf(stderr, "Error: Could not create TCP socket\n");
        return 1;
    }

    int status = amqp_socket_open(socket, AMQP_BROKER_HOST, AMQP_BROKER_PORT);
    if (status) {
        fprintf(stderr, "Error: Could not open TCP socket\n");
        return 1;
    }

    amqp_login(conn, "/", 0, 131072, 0, AMQP_SASL_METHOD_PLAIN, "RgRabbit", "ZSNVqEj9b2");
    amqp_channel_open(conn, 1);
    amqp_get_rpc_reply(conn);

    amqp_queue_declare_ok_t *r = amqp_queue_declare(conn, 1, amqp_cstring_bytes(AMQP_QUEUE_NAME), 0, 0, 0, 1, amqp_empty_table);
    amqp_basic_consume(conn, 1, amqp_cstring_bytes(AMQP_QUEUE_NAME), amqp_empty_bytes, 0, 1, 0, amqp_empty_table);
    amqp_get_rpc_reply(conn);

    while (1) {
        amqp_frame_t frame;
        int result = amqp_simple_wait_frame(conn, &frame);
        if (result < 0) {
            break;
        }

        if (frame.frame_type != AMQP_FRAME_METHOD) {
            continue;
        }

        if (frame.payload.method.id != AMQP_BASIC_DELIVER_METHOD) {
            continue;
        }

        amqp_basic_deliver_t *delivery = (amqp_basic_deliver_t *)frame.payload.method.decoded;
        printf("Message received: %.*s\n", (int)delivery->exchange.len, (char *)delivery->exchange.bytes);

        amqp_basic_ack(conn, 1, delivery->delivery_tag, 0);
    }

    amqp_channel_close(conn, 1, AMQP_REPLY_SUCCESS);
    amqp_connection_close(conn, AMQP_REPLY_SUCCESS);

    amqp_destroy_connection(conn);

    return 0;
}
