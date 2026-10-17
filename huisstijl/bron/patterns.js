/* DHC patronen, opgebouwd uit de vormen van het logo (eenheden van het logo: 1502 × 841). Werkt in de browser en in Node. */
const DHCPatterns = (() => {
  const PR = (typeof DHC_PARTS !== 'undefined') ? DHC_PARTS.parts : null;
  const MARK = parts => [parts.Dbowl, parts.Dbar, parts.Htop, parts.Hbot, parts.Cbowl, parts.Cbar].join(' ');
  function tile(kind, c, parts){
    const ev = `fill-rule="evenodd"`;
    if (kind === 'raster'){
      const w = 2102, h = 2682, m = MARK(parts);
      const at = (x, y, col) => `<path ${ev} fill="${col}" transform="translate(${x} ${y})" d="${m}"/>`;
      return {w, h, body: at(300, 250, c.fg) + at(1351, 1591, c.acc || c.fg) + at(1351 - w, 1591, c.acc || c.fg)};
    }
    if (kind === 'schakels'){
      const w = 1124, h = 1882;
      const pair = (x, y, col) => `<g fill="${col}" transform="translate(${x} ${y})"><path ${ev} transform="translate(-1020 0)" d="${parts.Cbowl}"/><path ${ev} transform="translate(542 0)" d="${parts.Dbowl}"/></g>`;
      return {w, h, body: pair(50, 50, c.fg) + pair(612, 991, c.acc || c.fg) + pair(612 - w, 991, c.acc || c.fg)};
    }
    // staven: het ritme van dunne staaf, open ruimte en H-blok, met de onderbreking telkens op een andere hoogte
    const unit = 499, cuts = [320, 90, 560, 210, 450], n = cuts.length, w = unit * n, h = 841;
    let body = '';
    cuts.forEach((y, i) => {
      const x = i * unit;
      body += `<rect x="${x}" y="0" width="39" height="${h}" fill="${i === 2 && c.acc ? c.acc : c.fg}"/>`;
      body += `<rect x="${x + 193}" y="0" width="152" height="${y}" fill="${c.fg}"/><rect x="${x + 193}" y="${y + 201}" width="152" height="${h - y - 201}" fill="${c.fg}"/>`;
    });
    return {w, h, body};
  }
  function svg(kind, c, scale = 0.1, W = 1200, H = 800, parts = PR){
    const t = tile(kind, c, parts), id = 'p' + kind;
    return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}"><defs><pattern id="${id}" patternUnits="userSpaceOnUse" width="${t.w}" height="${t.h}" patternTransform="scale(${scale})">${t.body}</pattern></defs><rect width="${W}" height="${H}" fill="${c.bg}"/><rect width="${W}" height="${H}" fill="url(#${id})"/></svg>`;
  }
  return {svg, tile};
})();
if (typeof module !== 'undefined') module.exports = DHCPatterns;
