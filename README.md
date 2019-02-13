# gj-union-web-app
Microservice for computing the union of GeoJSON features

[![Build Status](https://travis-ci.com/DHI-GRAS/gj-union-web-app.svg?token=xFUvaoqNvYGuqLz5TEdJ&branch=master)](https://travis-ci.com/DHI-GRAS/gj-union-web-app)
[![codecov](https://codecov.io/gh/DHI-GRAS/gj-union-web-app/branch/master/graph/badge.svg?token=iYyh1duDt5)](https://codecov.io/gh/DHI-GRAS/gj-union-web-app)


## API usage

POST JSON data of this format:

```json
{
  "geometries": [
    {
      "type": "Polygon",
      "coordinates": [
        [
          [
            38.814697265625,
            -6.817352822622144
          ],
          [
            39.9847412109375,
            -6.817352822622144
          ],
          [
            39.9847412109375,
            -5.413679614940935
          ],
          [
            38.814697265625,
            -5.413679614940935
          ],
          [
            38.814697265625,
            -6.817352822622144
          ]
        ]
      ]
    },
    {
      "type": "Polygon",
      "coordinates": [
        [
          [
            39.287109375,
            -5.626919311742117
          ],
          [
            40.1715087890625,
            -5.626919311742117
          ],
          [
            40.1715087890625,
            -4.691404288203818
          ],
          [
            39.287109375,
            -4.691404288203818
          ],
          [
            39.287109375,
            -5.626919311742117
          ]
        ]
      ]
    }
  ]
}
```

and get the union GeoJSON back, brought to you by Shapely / libgeos.


## Deployment

... is very easy thanks to Zappa: Remove the `.in` from `zappa_config.toml.in`
and ajust to your needs. Then `zappa deploy development`.


## Why?

Computing the union of complex polygons is expensive. If an app needs to do that many
times, you might be better off offloading this to a microservice that can run many times
in parallel and caches nicely.
