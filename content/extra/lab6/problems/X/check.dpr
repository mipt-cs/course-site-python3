uses testlib,SysUtils;

procedure swap(var a, b: longint);
var t: longint;
begin
    t := a;
    a := b;
    b := t
end;

function goodpair(a, b: longint): boolean;
begin
    goodpair := (a = b + 1) or (a = b - 1)
end;

const maxr = 3;
	  maxn = 10;
	  maxc = 200000;
var r:array [1..maxr,0..maxn] of longint;
	n,i,cc,ta,tb,tc:longint;
begin
 n:=inf.readlongint;
 r[1,0]:=n;
 for i:=1 to n do r[1,i]:=n-i+1;
 cc:=0;
 while not ouf.seekeof do
  begin
  inc(cc);
  if cc>maxc then quit(_pe,'Too many commands');
  ta:=ouf.readlongint;
  tb:=ouf.readlongint;
  tc:=ouf.readlongint;
  if (ta<0) or (ta>1) then quit(_pe,format('Wrong command ID at command #%d',[cc]));
  if (tb<1) or (tb>maxr) then quit(_pe,format('Wrong rod ID at command #%d',[cc]));
  if (tc<1) or (tc>maxr) then quit(_pe,format('Wrong rod ID at command #%d',[cc]));
  if ta = 1 then
  begin
      if (r[tb,0]=0) then quit(_wa,format('Rod #%d is empty at command #%d',[tb, cc]));
      if (r[tb,r[tb,0]]<>1) then quit(_wa,format('There is no disk 1 on rod #%d at command #%d',[tb,cc]));
      dec(r[tb,0]);
      inc(r[tc,0]);
      r[tc,r[tc,0]]:=1
  end
  else
  begin
      if (r[tb,0]=0) then quit(_wa,format('Rod #%d is empty at command #%d',[tb, cc]));
      if (r[tc,0]=0) then quit(_wa,format('Rod #%d is empty at command #%d',[tc, cc]));
      if not goodpair(r[tb,r[tb,0]], r[tc,r[tc,0]]) then quit(_wa,format('Disk moving breaks the rules of the game at command #%d',[cc]));
      swap(r[tb,r[tb,0]], r[tc,r[tc,0]]);
  end;
  end;
  if (r[maxr,0]<>n) then quit(_wa,'After all commands all disks are not on their places');
  quit(_ok,'Looks like correct');
end.
