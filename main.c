    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <mosquitto.h>

    #define MQTT_BROKER_HOST ""
    #define MQTT_BROKER_PORT 1883
    #define MQTT_TOPIC "main"
    #define MQTT_USERNAME ""
    #define MQTT_PASSWORD ""

    int main() {
        struct mosquitto *mosq = NULL;
        int rc = 0;

        mosquitto_lib_init();

        mosq = mosquitto_new(NULL, true, NULL);
        if (!mosq) {
            fprintf(stderr, "Error: Unable to initialize the Mosquitto library.\n");
            return 1;
        }

        // Set username and password
        mosquitto_username_pw_set(mosq, MQTT_USERNAME, MQTT_PASSWORD);

        mosquitto_connect(mosq, MQTT_BROKER_HOST, MQTT_BROKER_PORT, 60);

        const char *message_payload = "{\"imei\":\"89984320001874978265\",\"balance\":12,\"version\":1,\"battery\":9,\"ZFI\":1,\"ZFA\":1,\"MFA\":1,\"AFA\":1,\"BFA\":0,\"SFA\":0}";

        rc = mosquitto_publish(mosq, NULL, MQTT_TOPIC, strlen(message_payload), message_payload, 0, false);
        if (rc != MOSQ_ERR_SUCCESS) {
            fprintf(stderr, "Error: Unable to publish message.\n");
        } else {
            printf("Message published successfully.\n");
        }

        mosquitto_disconnect(mosq);
        mosquitto_destroy(mosq);
        mosquitto_lib_cleanup();

        return 0;
    }
