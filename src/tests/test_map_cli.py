import tempfile

import pytest


@pytest.fixture
def test_input_file():
    temp_tmx = tempfile.NamedTemporaryFile('w', suffix='.tmx')
    temp_tmx.write('''<?xml version="1.0" encoding="UTF-8"?>
<map version="1.2" tiledversion="1.3.2" orientation="orthogonal" renderorder="right-down" compressionlevel="-1" width="1" height="1" tilewidth="8" tileheight="8" infinite="0" nextlayerid="2" nextobjectid="1">
 <layer id="1" name="Tile Layer 1" width="1" height="1">
  <data encoding="csv">
1
</data>
 </layer>
</map>''')
    temp_tmx.flush()
    return temp_tmx


def test_map_tiled_cli_no_args():
    from ttblit import main

    with pytest.raises(SystemExit):
        main(['map'])


def test_map_tiled_cli(test_input_file):
    from ttblit import main

    with pytest.raises(SystemExit):
        main(['map', '--input_file', test_input_file.name, '--output_format', 'c_header'])
