# SecurityTrails Wrapper

This is a simple wrapper for the SecurityTrails API. It is a work in progress and is not yet complete.

1. Correct, see if the IP has changed for the listed domain. If it has, tell me somehow and tell me the new IP.
2. For each domain, look at the subdomains and mark all the subdomains and their related IPs. (these could just be new lines in a csv for each domain/ip)

while doing all of this, check if the IP you're looking at has like 50+ domains attached to it. If it is, mark it as "suspected CDN or shared host"

TODO:
- [x]  