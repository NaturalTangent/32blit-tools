
def test_font_image(test_resources):
    from ttblit.asset.builders import font
    image = open(test_resources / "8x8font.png", "rb").read()
    output = font.font.build(image, 'image')

    # header
    # char width
    # data...
    assert(output == (
        b'FONT\x60\x08\x08\x01'
        + b'\x03\x02\x04\x07\x06\x08\x07\x02\x03\x03\x05\x06\x03\x06\x02\x05\x06\x03\x05\x05\x06\x05\x06\x06\x06\x06\x02\x03\x05\x06\x05\x05\x07\x06\x06\x05\x06\x05\x05\x06\x06\x04\x06\x05\x05\x08\x06\x07\x06\x08\x06\x05\x06\x06\x06\x08\x06\x06\x06\x03\x05\x03\x04\x07\x03\x07\x05\x04\x05\x05\x04\x05\x05\x02\x04\x05\x04\x08\x05\x06\x05\x06\x04\x04\x05\x05\x06\x08\x06\x06\x06\x04\x02\x04\x05\x01'
        + b'\x00\x00\x00\x00\x00\x00\x00\x00\x5f\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x24\x7e\x24\x24\x7e\x24\x00\x00\x06\x49\x7f\x49\x30\x00\x00\x00\x43\x23\x10\x08\x04\x62\x61\x00\x36\x49\x49\x4e\x30\x48\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x3e\x41\x00\x00\x00\x00\x00\x00\x41\x3e\x00\x00\x00\x00\x00\x00\x12\x0c\x0c\x12\x00\x00\x00\x00\x10\x10\x7c\x10\x10\x00\x00\x00'
        + b'\x80\x40\x00\x00\x00\x00\x00\x00\x10\x10\x10\x10\x10\x00\x00\x00\x40\x00\x00\x00\x00\x00\x00\x00\xc0\x30\x0c\x03\x00\x00\x00\x00\x3e\x41\x41\x41\x3e\x00\x00\x00\x02\x7f\x00\x00\x00\x00\x00\x00\x61\x51\x49\x46\x00\x00\x00\x00\x49\x49\x49\x36\x00\x00\x00\x00\x0f\x10\x10\x7f\x10\x00\x00\x00\x4f\x49\x49\x31\x00\x00\x00\x00\x3e\x49\x49\x49\x31\x00\x00\x00\x01\x01\x61\x19\x07\x00\x00\x00'
        + b'\x36\x49\x49\x49\x36\x00\x00\x00\x06\x49\x49\x49\x3e\x00\x00\x00\x42\x00\x00\x00\x00\x00\x00\x00\x80\x42\x00\x00\x00\x00\x00\x00\x08\x14\x22\x41\x00\x00\x00\x00\x24\x24\x24\x24\x24\x00\x00\x00\x41\x22\x14\x08\x00\x00\x00\x00\x01\x59\x09\x06\x00\x00\x00\x00\x1c\x22\x49\x55\x55\x0e\x00\x00\x7e\x09\x09\x09\x7e\x00\x00\x00\x7f\x49\x49\x49\x36\x00\x00\x00\x3e\x41\x41\x41\x00\x00\x00\x00'
        + b'\x7f\x41\x41\x41\x3e\x00\x00\x00\x7f\x49\x49\x49\x00\x00\x00\x00\x7f\x09\x09\x09\x00\x00\x00\x00\x3e\x41\x41\x51\x71\x00\x00\x00\x7f\x08\x08\x08\x7f\x00\x00\x00\x41\x7f\x41\x00\x00\x00\x00\x00\x41\x41\x3f\x01\x01\x00\x00\x00\x7f\x08\x14\x63\x00\x00\x00\x00\x7f\x40\x40\x40\x00\x00\x00\x00\x7f\x02\x04\x08\x04\x02\x7f\x00\x7f\x06\x08\x30\x7f\x00\x00\x00\x3e\x41\x41\x41\x41\x3e\x00\x00'
        + b'\x7e\x09\x09\x09\x06\x00\x00\x00\x3e\x41\x41\x61\x41\xbe\x80\x00\x7f\x09\x09\x19\x66\x00\x00\x00\x46\x49\x49\x31\x00\x00\x00\x00\x01\x01\x7f\x01\x01\x00\x00\x00\x3f\x40\x40\x40\x3f\x00\x00\x00\x0f\x30\x40\x30\x0f\x00\x00\x00\x3f\x40\x40\x3c\x40\x40\x3f\x00\x63\x14\x08\x14\x63\x00\x00\x00\x03\x04\x78\x04\x03\x00\x00\x00\x61\x51\x49\x45\x43\x00\x00\x00\x7f\x41\x00\x00\x00\x00\x00\x00'
        + b'\x03\x0c\x30\xc0\x00\x00\x00\x00\x41\x7f\x00\x00\x00\x00\x00\x00\x02\x01\x02\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x01\x02\x00\x00\x00\x00\x00\x00\x38\x44\x44\x44\x38\x40\x00\x00\x7f\x44\x44\x38\x00\x00\x00\x00\x38\x44\x44\x00\x00\x00\x00\x00\x38\x44\x44\x7f\x00\x00\x00\x00\x38\x54\x54\x48\x00\x00\x00\x00\x7e\x09\x01\x00\x00\x00\x00\x00\x48\x94\x94\x78\x00\x00\x00\x00'
        + b'\x7f\x08\x08\x70\x00\x00\x00\x00\x7d\x00\x00\x00\x00\x00\x00\x00\x80\x80\x7d\x00\x00\x00\x00\x00\x7f\x10\x28\x44\x00\x00\x00\x00\x3f\x40\x40\x00\x00\x00\x00\x00\x78\x04\x04\x38\x04\x04\x78\x00\x78\x04\x04\x78\x00\x00\x00\x00\x38\x44\x44\x44\x38\x00\x00\x00\xfc\x24\x24\x18\x00\x00\x00\x00\x18\x24\x24\xfc\x40\x00\x00\x00\x78\x04\x04\x00\x00\x00\x00\x00\x48\x54\x24\x00\x00\x00\x00\x00'
        + b'\x08\x3e\x48\x40\x00\x00\x00\x00\x3c\x40\x40\x3c\x00\x00\x00\x00\x0c\x30\x40\x30\x0c\x00\x00\x00\x0c\x30\x40\x30\x40\x30\x0c\x00\x44\x28\x10\x28\x44\x00\x00\x00\x8c\x50\x20\x10\x0c\x00\x00\x00\x44\x64\x54\x4c\x44\x00\x00\x00\x08\x36\x41\x00\x00\x00\x00\x00\x7f\x00\x00\x00\x00\x00\x00\x00\x41\x36\x08\x00\x00\x00\x00\x00\x08\x04\x08\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
    ))
