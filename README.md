## C2 Toy

### Probe

```bash
hacker@node: python3 src/ctx.py
```

```bash
victim@node: python3 src/utils/payload.py
```

### Docker

```bash
# build
user@node: make build NAME='c2-toy:latest'

# remove
user@node: make rmi NAME='c2-toy:latest'
```