#!/usr/bin/python
#
# Copyright 2018-2020 Polyaxon, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# General
POLYAXON_KEYS_SERVICE = "POLYAXON_SERVICE"
POLYAXON_KEYS_HEADER = "POLYAXON_HEADER"
POLYAXON_KEYS_HEADER_SERVICE = "POLYAXON_HEADER_SERVICE"
POLYAXON_KEYS_AUTHENTICATION_TYPE = "POLYAXON_AUTHENTICATION_TYPE"
POLYAXON_KEYS_DEBUG = "POLYAXON_DEBUG"
POLYAXON_KEYS_TIMEOUT = "POLYAXON_TIMEOUT"
POLYAXON_KEYS_TRACKING_TIMEOUT = "POLYAXON_TRACKING_TIMEOUT"
POLYAXON_KEYS_TIME_ZONE = "POLYAXON_TIME_ZONE"
POLYAXON_KEYS_WATCH_INTERVAL = "POLYAXON_WATCH_INTERVAL"
POLYAXON_KEYS_INTERVAL = "POLYAXON_INTERVAL"
POLYAXON_KEYS_LOG_LEVEL = "POLYAXON_LOG_LEVEL"
POLYAXON_KEYS_K8S_NAMESPACE = "POLYAXON_K8S_NAMESPACE"
POLYAXON_KEYS_K8S_NODE_NAME = "POLYAXON_K8S_NODE_NAME"
POLYAXON_KEYS_K8S_POD_ID = "POLYAXON_K8S_POD_ID"
POLYAXON_KEYS_API_HOST = "POLYAXON_API_HOST"
POLYAXON_KEYS_API_VERSION = "POLYAXON_API_VERSION"
POLYAXON_KEYS_VERIFY_SSL = "POLYAXON_VERIFY_SSL"
POLYAXON_KEYS_SSL_CA_CERT = "POLYAXON_SSL_CA_CERT"
POLYAXON_KEYS_CERT_FILE = "POLYAXON_CERT_FILE"
POLYAXON_KEYS_KEY_FILE = "POLYAXON_KEY_FILE"
POLYAXON_KEYS_ASSERT_HOSTNAME = "POLYAXON_ASSERT_HOSTNAME"
POLYAXON_KEYS_CONNECTION_POOL_MAXSIZE = "POLYAXON_CONNECTION_POOL_MAXSIZE"
POLYAXON_KEYS_UPLOAD_SIZE_WARN = "POLYAXON_UPLOAD_SIZE_WARN"
POLYAXON_KEYS_UPLOAD_SIZE_MAX = "POLYAXON_UPLOAD_SIZE_MAX"
POLYAXON_KEYS_ARCHIVE_ROOT = "POLYAXON_ARCHIVE_ROOT"
POLYAXON_KEYS_STATIC_ROOT = "POLYAXON_STATIC_ROOT"
POLYAXON_KEYS_CONTEXT_ROOT = "POLYAXON_CONTEXT_ROOT"

# Secrets
POLYAXON_KEYS_SECRET_KEY = "POLYAXON_SECRET_KEY"  # noqa
POLYAXON_KEYS_SECRET_INTERNAL_TOKEN = "POLYAXON_SECRET_INTERNAL_TOKEN"  # noqa
POLYAXON_KEYS_AUTH_TOKEN = "POLYAXON_AUTH_TOKEN"
POLYAXON_KEYS_AUTH_USERNAME = "POLYAXON_AUTH_USERNAME"

# Containers
POLYAXON_KEYS_AGENT_INSTANCE = "POLYAXON_AGENT_INSTANCE"
POLYAXON_KEYS_RUN_INSTANCE = "POLYAXON_RUN_INSTANCE"
POLYAXON_KEYS_CONTAINER_ID = "POLYAXON_CONTAINER_ID"
POLYAXON_KEYS_HASH_LENGTH = "POLYAXON_HASH_LENGTH"

# Flags
POLYAXON_KEYS_K8S_IN_CLUSTER = "POLYAXON_K8S_IN_CLUSTER"
POLYAXON_KEYS_IS_MANAGED = "POLYAXON_IS_MANAGED"
POLYAXON_KEYS_IS_SERVICE = "POLYAXON_IS_SERVICE"
POLYAXON_KEYS_IS_LOCAL = "POLYAXON_IS_LOCAL"
POLYAXON_KEYS_IS_OFFLINE = "POLYAXON_IS_OFFLINE"
POLYAXON_KEYS_IS_OPS = "POLYAXON_IS_OPS"
POLYAXON_KEYS_NO_OP = "POLYAXON_NO_OP"
POLYAXON_KEYS_NO_API = "POLYAXON_NO_API"

# Registry
POLYAXON_KEYS_PUBLIC_REGISTRY = "POLYAXON_PUBLIC_REGISTRY"

# Agent
POLYAXON_KEYS_AGENT_SIDECAR = "POLYAXON_AGENT_SIDECAR"
POLYAXON_KEYS_AGENT_INIT = "POLYAXON_AGENT_INIT"
POLYAXON_KEYS_AGENT_ARTIFACTS_STORE = "POLYAXON_AGENT_ARTIFACTS_STORE"
POLYAXON_KEYS_AGENT_CONNECTIONS = "POLYAXON_AGENT_CONNECTIONS"
POLYAXON_KEYS_AGENT_NOTIFICATION_CONNECTIONS = "POLYAXON_AGENT_NOTIFICATION_CONNECTIONS"
POLYAXON_KEYS_AGENT_PATH = "POLYAXON_AGENT_PATH"
POLYAXON_KEYS_SET_AGENT = "POLYAXON_SET_AGENT"
POLYAXON_KEYS_K8S_APP_SECRET_NAME = "POLYAXON_K8S_APP_SECRET_NAME"  # noqa
POLYAXON_KEYS_AGENT_SECRET_NAME = "POLYAXON_AGENT_SECRET_NAME"  # noqa
POLYAXON_KEYS_AGENT_RUNS_SA = "POLYAXON_AGENT_RUNS_SA"

# Connections
POLYAXON_KEYS_COLLECT_ARTIFACTS = "POLYAXON_COLLECT_ARTIFACTS"
POLYAXON_KEYS_COLLECT_RESOURCES = "POLYAXON_COLLECT_RESOURCES"
POLYAXON_KEYS_ARTIFACTS_STORE_NAME = "POLYAXON_ARTIFACTS_STORE_NAME"
POLYAXON_KEYS_GIT_CREDENTIALS = "POLYAXON_GIT_CREDENTIALS"
POLYAXON_KEYS_SSH_PATH = "POLYAXON_SSH_PATH"
POLYAXON_KEYS_CONNECTION_CONTEXT_PATH_FORMAT = "POLYAXON_CONNECTION_CONTEXT_PATH_{}"
POLYAXON_KEYS_CONNECTION_SCHEMA_FORMAT = "POLYAXON_CONNECTION_SCHEMA_{}"

# Ops
POLYAXON_KEYS_ISTIO_ENABLED = "POLYAXON_ISTIO_ENABLED"
POLYAXON_KEYS_SPARK_ENABLED = "POLYAXON_SPARK_ENABLED"
POLYAXON_KEYS_DASK_ENABLED = "POLYAXON_DASK_ENABLED"
POLYAXON_KEYS_FLINK_ENABLED = "POLYAXON_FLINK_ENABLED"
POLYAXON_KEYS_TFJOB_ENABLED = "POLYAXON_TFJOB_ENABLED"
POLYAXON_KEYS_PYTORCH_JOB_ENABLED = "POLYAXON_PYTORCH_JOB_ENABLED"
POLYAXON_KEYS_MPIJOB_ENABLED = "POLYAXON_MPIJOB_ENABLED"

# Proxies
POLYAXON_KEYS_PROXY_NAMESPACES = "POLYAXON_PROXY_NAMESPACES"
POLYAXON_KEYS_PROXY_STREAMS_PORT = "POLYAXON_PROXY_STREAMS_PORT"
POLYAXON_KEYS_PROXY_STREAMS_HOST = "POLYAXON_PROXY_STREAMS_HOST"
POLYAXON_KEYS_PROXY_API_PORT = "POLYAXON_PROXY_API_PORT"
POLYAXON_KEYS_PROXY_API_HOST = "POLYAXON_PROXY_API_HOST"
POLYAXON_KEYS_PROXY_API_USE_RESOLVER = "POLYAXON_PROXY_API_USE_RESOLVER"
POLYAXON_KEYS_PROXY_SERVICES_PORT = "POLYAXON_PROXY_SERVICES_PORT"
POLYAXON_KEYS_PROXY_SSL_PATH = "POLYAXON_PROXY_SSL_PATH"
POLYAXON_KEYS_PROXY_SSL_ENABLED = "POLYAXON_PROXY_SSL_ENABLED"
POLYAXON_KEYS_PROXY_SERVICES = "POLYAXON_PROXY_SERVICES"
POLYAXON_KEYS_PROXY_AUTH_ENABLED = "POLYAXON_PROXY_AUTH_ENABLED"
POLYAXON_KEYS_PROXY_AUTH_EXTERNAL = "POLYAXON_PROXY_AUTH_EXTERNAL"
POLYAXON_KEYS_PROXY_AUTH_USE_RESOLVER = "POLYAXON_PROXY_AUTH_USE_RESOLVER"
POLYAXON_KEYS_DNS_USE_RESOLVER = "POLYAXON_DNS_USE_RESOLVER"
POLYAXON_KEYS_DNS_CUSTOM_CLUSTER = "POLYAXON_DNS_CUSTOM_CLUSTER"
POLYAXON_KEYS_DNS_BACKEND = "POLYAXON_DNS_BACKEND"
POLYAXON_KEYS_DNS_PREFIX = "POLYAXON_DNS_PREFIX"
POLYAXON_KEYS_NGINX_TIMEOUT = "POLYAXON_NGINX_TIMEOUT"
POLYAXON_KEYS_NGINX_INDENT_CHAR = "POLYAXON_NGINX_INDENT_CHAR"
POLYAXON_KEYS_NGINX_INDENT_WIDTH = "POLYAXON_NGINX_INDENT_WIDTH"
