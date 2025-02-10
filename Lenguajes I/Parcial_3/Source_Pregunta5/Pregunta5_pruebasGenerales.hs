foldrM :: (a -> b -> b) -> b -> [a] -> b
foldrM _ e [] = e
foldrM f e (x:xs) = f x $ foldrM f e xs

const1 :: a -> b -> a
const1 x _ = x

what :: a -> ([b] -> [(a, b)]) -> [b] -> [(a, b)]
what _ _ [] = []
what x f (y:ys) = (x, y) : f ys

misteriosa :: [a] -> [b] -> [(a, b)]
misteriosa = foldrM what (const1 [])

gen :: Int -> [Int]
gen n = n : gen (n + 1)

-- Parte b del solucionario.
{-
Considere el siguiente tipo de datos que representa árboles binarios con información
en las ramas:
data Arbol a = Hoja | Rama a (Arbol a) (Arbol a)
Construya una función foldA (junto con su firma) que permita reducir un valor de
tipo (Arbol a) a algún tipo b (de forma análoga a foldr). Su implementación debe
poder tratar con estructuras potencialmente infinitas.
Su función debe cumplir con la siguiente firma:
foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b
-}

data Arbol a = Hoja | Rama a (Arbol a) (Arbol a)

foldA :: (a -> b -> b -> b) -> b -> Arbol a -> b
foldA _ e Hoja = e
foldA f e (Rama x a b) = f x (foldA f e a) (foldA f e b)

-- Parte c del solucionario.
{-
Considere una versión de la función what que funciona sobre árboles (aplica la función
proporcionada a ambos sub–árboles) y llamésmola what tree function:
-}

whatTF :: a
    -> (Arbol b -> Arbol (a, b))
    -> (Arbol b -> Arbol (a, b))
    -> Arbol b
    -> Arbol (a, b)
whatTF _ _ _ Hoja = Hoja
whatTF x f g (Rama y i d) = Rama (x, y) (f i) (g d)

{-
Usando su función foldA definimos la función sospechosa:
-}

sospechosa :: Arbol a -> Arbol b -> Arbol (a, b)
sospechosa = foldA whatTF (const Hoja)

{-
Definimos también la siguiente función, que genera un árbol de números enteros a
partir de un cierto valor inicial:
-}
genA :: Int -> Arbol Int
genA n = Rama n (genA (n + 1)) (genA (n * 2))

{-
Finalmente, definimos el valor "arbolito" como una instancia de Arbol Char:
-}

arbolito :: Arbol Char
arbolito = Rama 'a' (Rama 'b' Hoja (Rama 'c' Hoja Hoja)) Hoja

{-
Muestre la evaluación, paso a paso, de la expresión sospechosa arbolito (genA 1),
considerando que:
i. El lenguaje tiene orden de evaluación normal.
ii. El lenguaje tiene orden de evaluación aplicativo.
-}


