# glowstick

[![Build Status](https://travis-ci.org/rsenk330/glowstick.png?branch=master)](https://travis-ci.org/rsenk330/glowstick)

Glowstick is a web application that controls [hdhomerun](http://www.silicondust.com/) devices.

Python >= 3.3 is required.

## Development

All python dependencies are defined in the requirements.txt file. Simply use pip to install them.

Note: A virtualenv is highly recommended.

```sh
$ mkvirtualenv -p python3 glowstick
$ pip install -r requirements-devel.txt
```

### Build Requirements

There are a few extra dependencies from npm:

* less
* autoprefixer

```sh
$ npm install -g less autoprefixer
```

### Testing

[tox](http://tox.readthedocs.org/en/latest/) is used to help automate the testing on various
versions of python (for now, only Python 3.3). To run the tests, simply run:

```sh
$ tox
```

## Contributing

1. [Fork it!](https://help.github.com/articles/fork-a-repo)
2. Create your feature branch (`git checkout -b my-new-formula`)
3. Commit your changes (`git commit -am 'Added some formula'`)
4. Push to the branch (`git push origin my-new-formula`)
