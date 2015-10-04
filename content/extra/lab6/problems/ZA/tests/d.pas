program about_hanoi_tower;

{  solution for task 3. "About Hanoi Towers"  }
{  written by Korchyomkin Maxim               }


type
  THanoiTower = array [1..50000] of byte;

var
  tower: THanoiTower;

const
  answer: array [false..true] of string = ('NO', 'YES');

procedure OpenFiles;
begin
end;

procedure CloseFiles;
begin
end;

procedure init(var n: longint);
var
  i: longint;
begin
  read(n);
  for i := 1 to n do read(tower[i]);
end;

procedure done(const i: boolean);
begin
  writeln(answer[i]);
end;

function testing(q: longint; s, t: byte): boolean;
begin
  testing := true;
  while q>0 do
    if tower[q] = s then begin
      dec(q);
      t := 6-s-t;
    end
    else if tower[q] = t then begin
      dec(q);
      s := 6-s-t;
    end
    else begin
      testing := false;
      exit;
    end;
end;

var
  q, i, _from, _to: byte;
  n: longint;

begin
  openFiles;
  init(n);
  read(q);
  for i := 1 to q do begin
    read(_from, _to);
    done( testing(n, _from, _to) );
  end;
  closeFiles;
end.