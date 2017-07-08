FROM nginx:1

EXPOSE 80
EXPOSE 443

COPY . .
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD ["nginx", "-g", "daemon off;"]
ENTRYPOINT ["/entrypoint.sh"]