import fs from "fs";
import { ISO_CSS } from "./kit/iso-kit.mjs";
import { EXTRA_CSS } from "./build.mjs";
const assets = fs.readFileSync("assets.json","utf8");
const css = JSON.stringify(ISO_CSS + EXTRA_CSS);
const app = fs.readFileSync("app.html","utf8");
const out = app.replace("/*DATA*/", () => `const ASSETS = ${assets};\nconst ISO_CSS = ${css};`);
fs.writeFileSync("dhc-contentstudio.html", out);
console.log("ok", out.length);
