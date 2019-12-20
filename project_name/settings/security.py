# Whether to use a secure cookie for the session cookie. If this is set to True, 
# the cookie will be marked as “secure”, which means browsers may ensure that 
# the cookie is only sent under an HTTPS connection.
#
# Leaving this setting off isn’t a good idea because an attacker could capture 
# an unencrypted session cookie with a packet sniffer and use the cookie to 
# hijack the user’s session.
SESSION_COOKIE_SECURE = True

# If True, the SecurityMiddleware sets the X-XSS-Protection: 1; mode=block 
# header on all responses that do not already have it.
#
# Modern browsers don’t honor X-XSS-Protection HTTP header anymore. Although 
# the setting offers little practical benefit, you may still want to set the 
# header if you support older browsers.
SECURE_BROWSER_XSS_FILTER = True

# If True, the SecurityMiddleware sets the X-Content-Type-Options: nosniff 
# header on all responses that do not already have it.
SECURE_CONTENT_TYPE_NOSNIFF = True

###### DANGER: Read about HTTP Strict Transport Security #######################

# If True, the SecurityMiddleware adds the includeSubDomains directive to the 
# HTTP Strict Transport Security header. It has no effect unless 
# SECURE_HSTS_SECONDS is set to a non-zero value.
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# If set to a non-zero integer value, the SecurityMiddleware sets the HTTP 
# Strict Transport Security header on all responses that do not already have it.
SECURE_HSTS_SECONDS = 60 # Manually increase after ensuring safe environment.,
# The max-age must be at least 31536000 seconds (1 year). <- https://hstspreload.org

# If True, the SecurityMiddleware adds the preload directive to the HTTP Strict 
# Transport Security header. It has no effect unless SECURE_HSTS_SECONDS is set 
# to a non-zero value.
SECURE_HSTS_PRELOAD = False # change to True after SECURE_HSTS_SECONDS = 31536000

###### DANGER: Read about HTTP Strict Transport Security #######################

# This tells Django to trust the X-Forwarded-Proto header that comes from our 
# proxy, and any time its value is 'https', then the request is guaranteed to 
# be secure (i.e., it originally came in via HTTPS).
#
# You should only set this setting if you control your proxy or have some other 
# guarantee that it sets/strips this header appropriately.
#
# Note that the header needs to be in the format as used by request.META – all 
# caps and likely starting with HTTP_. (Remember, Django automatically adds 
# 'HTTP_' to the start of x-header names before making the header available in 
# request.META.)
#
# Modifying this setting can compromise your site’s security. Ensure you fully 
# understand your setup before changing it.
#
# Make sure ALL of the following are true before setting this (assuming the 
# values from the example above):
#
#    * Your Django app is behind a proxy.
#    * Your proxy strips the X-Forwarded-Proto header from all incoming requests. 
#      In other words, if end users include that header in their requests, the 
#      proxy will discard it.
#    * Your proxy sets the X-Forwarded-Proto header and sends it to Django, but 
#       only for requests that originally come in via HTTPS.
#
# If any of those are not true, you should keep this setting set to None and 
# find another way of determining HTTPS, perhaps via custom middleware.
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# If a URL path matches a regular expression in this list, the request will not 
# be redirected to HTTPS. The SecurityMiddleware strips leading slashes from URL
# paths, so patterns shouldn’t include them, e.g. 
# SECURE_REDIRECT_EXEMPT = [r'^no-ssl/$', ...]. 
#
# If SECURE_SSL_REDIRECT is False, this setting has no effect.
SECURE_REDIRECT_EXEMPT = []

# Django 3.0+
# If configured, the SecurityMiddleware sets the Referrer Policy header on all 
# responses that do not already have it to the value provided.
SECURE_REFERRER_POLICY = None

# If a string (e.g. secure.example.com), all SSL redirects will be directed to 
# this host rather than the originally-requested host (e.g. www.example.com). 
# If SECURE_SSL_REDIRECT is False, this setting has no effect.
SECURE_SSL_HOST = False

# If True, the SecurityMiddleware redirects all non-HTTPS requests to HTTPS 
# (except for those URLs matching a regular expression listed in 
# SECURE_REDIRECT_EXEMPT).
#
# If turning this to True causes infinite redirects, it probably means your site
# is running behind a proxy and can’t tell which requests are secure and which 
# are not. Your proxy likely sets a header to indicate secure requests; you can 
# correct the problem by finding out what that header is and configuring the 
# SECURE_PROXY_SSL_HEADER setting accordingly.
SECURE_SSL_REDIRECT = False # Set to true after ensuring nginx/proxy config.
