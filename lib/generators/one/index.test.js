const generator1 = require('./index');
const {floor, PI} = Math;
describe('1 + (floor(n * PI^11) % 100)', () => {
  it('n = 1', () => {
    const n = 1;
    expect(floor(n * PI**11)).toBe(294204);
    expect(generator1(n)).toBe(5);
  });
  it('n = 150', () => {
    const n = 150;
    expect(floor(n * PI**11)).toBe(44130602);
    expect(generator1(n)).toBe(3);
  });  
  it('n = 300', () => {
    const n = 300;
    expect(floor(n * PI**11)).toBe(88261205);
    expect(generator1(n)).toBe(6);
  });  
});