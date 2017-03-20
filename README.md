# munin-rocketchat

Three Munin plugins to query some useful information of a RocketChat server.

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/frdmn/munin-rocketchat /opt/munin-rocketchat
    ```

2. Install the project dependencies:

    ```
    cd /opt/munin-rocketchat
    pip install -r requirements.txt
    ```

3. Adjust API credentials and server information in `plugin-conf.d`:

    ```
    cp  plugin-conf.d/rocketchat /etc/munin/plugin-conf.d/rocketchat
    vi /etc/munin/plugin-conf.d/rocketchat
    ```

## Usage

Symlink the plugins you need into your `/etc/munin/plugins` directory:

```
ln -sf /opt/munin-rocketchat/scripts/rocketchat_* /etc/munin/plugins/
```

## Contributing

1. Fork it
2. Create your feature branch: `git checkout -b feature/my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/my-new-feature`
5. Submit a pull request

## Requirements / Dependencies

* Munin
* Python

## Version

1.1.0

## License

[MIT](LICENSE)
