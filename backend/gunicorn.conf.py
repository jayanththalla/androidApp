# Gunicorn configuration file for memory optimization
import multiprocessing

# Number of worker processes
workers = 1  # Reduce to 1 worker to minimize memory usage

# Worker class
worker_class = 'sync'  # Use sync worker class for better memory management

# Timeout settings
timeout = 120  # Increase timeout for large file processing

# Memory settings
max_requests = 10  # Restart workers after 10 requests to prevent memory leaks
max_requests_jitter = 5  # Add jitter to prevent all workers from restarting at once

# Logging
accesslog = '-'  # Log to stdout
errorlog = '-'   # Log to stderr
loglevel = 'info'

# Process naming
proc_name = 'android-app-analyzer'

# Preload application
preload_app = True

# Worker connections
worker_connections = 1000

# Keep-alive
keepalive = 5

# Limit request body size
limit_request_line = 0
limit_request_fields = 100
limit_request_field_size = 8190 