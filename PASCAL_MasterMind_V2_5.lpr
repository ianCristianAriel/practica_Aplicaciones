program MasterMind_V2_5;
const MAX_INTENTOS = 10; //Cantidad máxima de intentos.
      LARGO_CODIGO = 4; //El largo de los códigos.
      PRIMERA_LETRA = 'A'; //  Letra inicial del rango disponible.
      ULTIMA_LETRA = 'H'; //Última letra del rango disponible.

type
//Subrango para restringir las letras que se pueden usar.
TLetras= PRIMERA_LETRA..ULTIMA_LETRA;
//Arreglo de letras con cantidad de celdas LARGO_CODIGO.
TCodigo= array[1..LARGO_CODIGO] of TLetras;

{Genera un código al azar y lo asigna a la variable codigo. El codigo generado
puede contener letras repetidas.}
procedure generarCodigo(var codigo:TCodigo);
var i, indice:byte;
    letra: char;
begin
randomize;
for I:=1 to LARGO_CODIGO do begin
indice:= random(ord(ULTIMA_LETRA)-ord(PRIMERA_LETRA)+1)+ord(PRIMERA_LETRA);
letra:=chr(indice);
codigo[i]:= letra;
end;
end;

{Lee el codigo de la entrada estandar y lo asigna a la variable codigo.
Ademas retorna el valor TRUE si el codigo leido es correcto, FALSE sino.
El codigo leido puede ser incorrecto si:
* Contiene uno o mas caracteres fuera del rango.
* No contiene el largo LARGO_CODIGO.}
function leerCodigo(var codigo: TCodigo): boolean;
var c: char;
    cLetras, i: byte;
    codigoI: string;
begin
cLetras:=0;
readln(codigoI);
for c in codigoI do begin
 if (c<PRIMERA_LETRA) or (c>ULTIMA_LETRA) or (cLetras>LARGO_CODIGO) then begin
  result:=false;
  exit;
  end;
 cLetras+=1;
 end;
 if (cLetras<Largo_codigo) then begin
  result:=false;
  exit;
  end;
  result:=true;
 for i:=1 to largo_codigo do begin
  codigo[i]:=codigoI[i];
  end;
end;

{Imprime el codigo pasado como argumento en la salida estandar. Deja el
cursor al final de esa misma línea.}
procedure imprimirCodigo(codigo: TCodigo);
begin
if not leerCodigo() then begin
writeln('ERROR: El codigo no es valido. Ingresa otro con ',largo_codigo,' letras entre ',PRIMERA_LETRA,' y ',ULTIMA_LETRA,'>>');
leerCodigo();
end;
intento+=1;
end;

{Calcula las notas de codAdivinador en función de codPensador. Asigna
los buenos y los regulares a los argumentos con el mismo nombre.}
procedure calcularNota(codAdivinador, codPensador: TCodigo; var buenos,
regulares: byte);
begin
for H:=1 to max_intentos do begin
Buenos:=0;//Se inicializa el contador de asiertos buenos en 0
Regulares:=0; //Se inicializa el contador de asiertos regulares en 0


for g:=1 to LARGO_CODIGO do begin
evaluadasP[g]:=false;
evaluadasA[g]:=false;
end;

for i:=1 to LARGO_CODIGO do begin
  read(codAdivinador[i]);
  if (codPensador[I]=codAdivinador[I]) then begin
   evaluadasP[I]:=true;
   evaluadasA[i]:=true;
   buenos+=1;
   end;
  end;

 for j:=1 to LARGO_CODIGO do begin
  if not evaluadasP[j] then begin
   for k:=1 to LARGO_CODIGO do begin
    if not evaluadasA[k] then begin
     if (codPensador[j]=codAdivinador[k]) then begin
     regulares+=1;
     evaluadasA[k]:= true;
     evaluadasP[j]:=true;
     end;
    end;
   end;
  end;
end;

writeln('B: ',buenos,'  '+'R: ',regulares);

if buenos=4 then begin
writeln('EXCELENTE!!! Ganaste.');
ganaste:=true;
break;
end;

if (H=MAX_INTENTOS) and not ganaste then BEGIN
writeln('PERDISTE!!! El codigo era: ');
 for m:=1 to LARGO_CODIGO do begin
 write(cod_pensador[m]);
 end;
 end;
READLN;
end;
end;
var   g, h, i, j, k, m, indice, intento, regulares, buenos: byte;
      letra: char;
      ganaste, perdiste: boolean;
      codPensador, codAdivinador: TCodigo;
      evaluadasP, evaluadasA: array[1..LARGO_CODIGO] of boolean;

begin

{Se inicializan las variables booleanas encargadas de detectar cuando se gana,
pierde.. y los intentos}
ganaste:=false;
perdiste:=false;
intento:=1;

generarCodigo();

{Se muestra el mensaje de entrada}
write('MasterMind V1.0'+#13#10);
writeln('Dispones de ',MAX_INTENTOS,' intentos para adivinar el codigo.');
write('Ingresa ',LARGO_CODIGO,' letras entre "',PRIMERA_LETRA,'" y "',ULTIMA_LETRA,'". Codigo ',intento,' de ',MAX_INTENTOS,'>>');

leerCodigo(codigo);

imprimirCodigo();

calcularLasNotas();

readln;

end.
