"""Threshold and connected-component localization for tiny synthetic PGM pages."""
from __future__ import annotations
import json
from collections import deque
from pathlib import Path

def read_pgm(path):
    parts=[p for line in path.read_text(encoding="ascii").splitlines() if not line.startswith("#") for p in line.split()]
    if parts[0] != "P2": raise ValueError("Only ASCII PGM (P2) is supported")
    width,height,maximum=map(int,parts[1:4]); pixels=list(map(int,parts[4:]));
    if len(pixels)!=width*height or maximum<=0: raise ValueError("Invalid PGM")
    return width,height,pixels

def localize(path, threshold=128, min_area=4):
    width,height,pixels=read_pgm(path); dark={(x,y) for y in range(height) for x in range(width) if pixels[y*width+x] < threshold}; boxes=[]
    while dark:
        start=dark.pop(); queue=deque([start]); points=[start]
        while queue:
            x,y=queue.popleft()
            for q in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if q in dark: dark.remove(q); queue.append(q); points.append(q)
        if len(points)>=min_area:
            xs=[p[0] for p in points]; ys=[p[1] for p in points]
            boxes.append([min(xs),min(ys),max(xs)-min(xs)+1,max(ys)-min(ys)+1])
    return sorted(boxes)

def iou(a,b):
    ax2,ay2=a[0]+a[2],a[1]+a[3]; bx2,by2=b[0]+b[2],b[1]+b[3]
    area=max(0,min(ax2,bx2)-max(a[0],b[0]))*max(0,min(ay2,by2)-max(a[1],b[1]))
    return area/(a[2]*a[3]+b[2]*b[3]-area) if area else 0.0

def redact(path, boxes):
    width,height,pixels=read_pgm(path); out=list(pixels)
    for x,y,w,h in boxes:
        for yy in range(y,y+h):
            for xx in range(x,x+w): out[yy*width+xx]=128
    return {"width":width,"height":height,"redacted_pixels":sum(p==128 for p in out)}

def evaluate(page, expected_path):
    expected=json.loads(expected_path.read_text(encoding="utf-8"))["boxes"]; predicted=localize(page)
    matches=[max((iou(p,e) for e in expected),default=0.0) for p in predicted]
    return {"image_format":"P2 PGM","image_size":[read_pgm(page)[0],read_pgm(page)[1]],"expected_boxes":expected,"predicted_boxes":predicted,"mean_best_iou":sum(matches)/len(expected),"redaction":redact(page,predicted)}
if __name__=="__main__":
    base=Path(__file__).with_name("data"); print(json.dumps(evaluate(base/"synthetic-page.pgm",base/"expected.json"),indent=2))
