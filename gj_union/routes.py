import shapely.ops
import shapely.geometry

from flask import request, jsonify, Blueprint

bp = Blueprint('routes', __name__, url_prefix='/')


def _parse_geometry_string(gs):
    try:
        return shapely.geometry.shape(gs)
    except (TypeError, ValueError) as err:
        raise ValueError(
            f'Unable to parse your geometry string in {gs}. '
            f'Make sure it is valid GeoJSON. ({err})'
        )


@bp.route('/', methods=['POST'])
def main():
    content = request.json
    if content is None or 'geometries' not in content:
        return (
            (
                'You must POST a JSON query like '
                '{"geometries": [{"type": "Polygon", "coordinates": "..."}, {...}]'
            ),
            400
        )

    geoms = []
    for gstr in content['geometries']:
        try:
            geoms.append(
                _parse_geometry_string(gstr)
            )
        except ValueError as err:
            return str(err), 400

    union = shapely.ops.unary_union(geoms)
    union_gj = shapely.geometry.mapping(union)
    return jsonify(union_gj), 200
