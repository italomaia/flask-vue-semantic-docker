FROM nginx:1

COPY . .
RUN chmod +x /root/entrypoint.sh
CMD ["nginx", "-g", "daemon off;"]
ENTRYPOINT ["/root/entrypoint.sh"]