const generator2 = require('./index');
const {floor, E} = Math;
describe('1 + (floor(n * e^11) % 100)', () => {
  it('n = 1', () => {
    const n = 1;
    expect(floor(n * E**11)).toBe(59874);
    expect(generator2(n)).toBe(75);
  });
  it('n = 150', () => {
    const n = 150;
    expect(floor(n * E**11)).toBe(8981121);
    expect(generator2(n)).toBe(22);
  });
  it('n = 300', () => {
    const n = 300;
    expect(floor(n * E**11)).toBe(17962242);
    expect(generator2(n)).toBe(43);
  });
});