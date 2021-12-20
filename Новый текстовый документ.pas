program lab1;
const e = power(10,-3);
const xmax = 3;
const xmin = 1;
var x,d,res:real;

function fun(x:real):real;
var res:real;
begin
res:= 3*sqr(ln(x))+6*ln(x)-5;
fun:= res;
end;

function funP(x:real):real;
var res:real;
begin
res:= (6*ln(x)+6)/x;
funP:= res;
end;

function calc(x:real;c:integer):real;
var d:real;
begin
  c+=1;

d:=fun(x)/funp(x);
if (abs(d)>e) then begin
res:=calc(x-d,c);
end
else
  writeln('итераций:',c);
res:=x-d;
calc := res;

end;

begin
x:=2;
res:=calc(x,1);
writeln(' x0 = ',res:10:7,' f(x0) = ',fun(res):10:7);
end.
