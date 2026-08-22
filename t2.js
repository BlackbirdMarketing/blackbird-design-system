const pptxgen = require("pptxgenjs");
const p = new pptxgen(); const s = p.addSlide();
const v = [
 ["none-str",       {line:"none"}],
 ["type none",      {line:{type:"none"}}],
 ["color none",     {line:{color:"none"}}],
 ["transparency100",{line:{color:"008C95",transparency:100}}],
 ["width 0 type none",{line:{width:0,type:"none"}}],
 ["omitted",        {}],
 ["dashType none",  {line:{dashType:"none"}}],
];
v.forEach((o,i)=>s.addShape(p.shapes.RECTANGLE,Object.assign({x:0,y:i*0.4,w:2,h:0.2,fill:{color:"008C95"}},o[1])));
p.writeFile({fileName:"t2.pptx"}).then(()=>console.log(v.map(x=>x[0]).join("|")));
