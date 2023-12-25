import turtle as kame #turtlをインポートしてkameする
kame.bgcolor('black')#背景を黒に変更

t=kame.Turtle()#オブジェクト作成
t.shape('turtle')#亀さん登場
t.speed(0)#亀さん最高速度

t.pencolor('red')#ペンの色を赤に変更
t.fillcolor('yellow')#黄色で塗りつぶす
t.begin_fill()#塗りつぶし開始
for i in range(36):#亀さん３６回動かす
    t.circle(190,90)#半径１９０の円を９０度分だけ書く
    t.left(90)#左に９０度回転
    t.circle(190,90)#半径１９０の円を９０度分だけ書く
    t.left(16)#左に１６度回転
t.end_fill()#塗りつぶし終わり

t.color('brown')#ペンの色を茶色に変更
for i in range(110):#１１０回亀さん動かす
    t.circle(100)#半径１００の円を描く
    t.left(7)#左に７度動く


t.pencolor('indigo')#ペンの色を藍に変更
t.pensize(3)#ペンのサイズを３に変更
for i in range(12):#１２回亀さん動かす
    t.circle(75)#半径７５の円を描く
    t.right(40)#右に４０度動く
    
t.pencolor('green')#ペンの緑をに変更
t.pensize(1)#ペンのサイズを１に変更
for i in range(50):#亀さん５０回動かす
    t.circle(210-i,90)#半径２１０からⅰだけ引いた円を９０度分だけ書く
    t.left(90)#左に９０度回転
    t.circle(210-i,90)#半径２１０からⅰだけ引いたの円を９０度分だけ書く
    t.left(18)#左に１８度回転 
    

    
t.pencolor('silver')#ペンの色をシルバーに変更
for i in range(52):#５２回亀さん動かす
    t.circle(30)#半径３０の円を描く
    t.left(10)#左に１０度動く
 
kame.done()#亀さんの終了
