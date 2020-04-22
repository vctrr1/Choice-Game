#DEFININDO OS PERSONAGENS 
define narrador = Character("Senhora da Floresta")
define ana = Character("Ana")
define amanda = Character("Amanda")
define cavaleiro = "Davi"
define estatua = Character ("Senhora de Ferro")
define maria = "Maria"

#DEFINIÇÃO DAS IMAGENS DOS PERSONAGENS

#IMAGENS DE AMANDA
image amanda1 = "amanda1.png"
image amanda2 = "amanda2.png"
image amandamorta = "amandamorta.png"
image amandachora = "amandachora.png"

#IMAGENS DE ANA
image ana1 = "anatriste.png"
image ana2 = "ana.png"
image ana3 = "ana3.png"
image anamorta = "anamorta.png"

#IMAGENS DOS DESAFIOS
image estatua1 = "senhora.png"
image monstro = "monstro.png"

#IMAGENS DE MARIA
image maria1 = "maria1.png"
image mariaraiva = "mariaraiva.png"
image mariaespelhada = "mariaespelhada.png"
image maria3 = "maria3.png"
image mariamorta = "mariamorta.png"

#IMAGENS DE DAVI
image cavaleiro1 = "Davi1.png"
image cavaleirosad = "cavaleiro_Triste.png"
image cavaleiroraiva = "cavaleiroraiva.png"
image cavaleirochora = "cavaleirochora.png"
image davimorto ="davimorto.png"

#IMAGENS DO NARRADOR
image narrador1 = "velha.png" 
image narrador2 = "velha2.png"

#DEFINIÇÃO DE CENÁRIOS
image fundofloresta = "fundoFloresta.png"
image cenario1 = "im1.png"
image cenario5 = "fila.png"
image cenario6 = "floresta1.png"
image escolha1 = "escolha1.png"
image cenario7 = "floresta5.png"
image lago1 = "lago.png"
image escolha2 = "2escolha.png"
image lago2= "lago2.png"
image escolhafinal = "escolhafinal.png"
image escolha22 = "2escolha2.png"
image escolha23 = "2escolha3.png"
image escolha24 = "2escolha4.png"
image escolhafinal2 ="escolhafinal2.png"
image escolhafinal3 = "escolhafinal3.png"
image escolhafinal12 = "escolha12.png"
image escolhafinal13 = "escolha13.png"
image escolhafinal14 = "escolha14.png"
image escolhafinal15 = "escolha15.png"

#DEFINIÇÃO DOS VÍDEOS
image fonte movie = Movie(size=(1280, 720),play="fonte0.mpg", mask="fonte0.mpg")
image portal movie = Movie(size=(1280, 720),play="portal.mpg", mask="portal.mpg")
image entrada movie = Movie(size=(1280, 720),play="entrada.mpg", mask="entrada.mpg")
image analider movie = Movie(size=(1280, 720),play="analider.mpg", mask="analider.mpg")
image davisumiu movie = Movie(size=(1280, 720),play="davi_desaparece.mpg", mask="davi_desaparece.mpg")
image fontefinal movie = Movie(size=(1280, 720),play="fontefinal.mpg", mask="fontefinal.mpg")
image amandavenceu movie = Movie(size=(1280, 720),play="amandavenceu.mpg", mask="amandavenceu.mpg")

# O JOGO COMEÇA AQUI
label start:
    play music "somJogo.mp3"
    #Vidas dos personagens 
    $amandavida = False
    $anavida = False
    $mariavida = False
    $davivida = False

    scene cenario1
    with dissolve
    show narrador1 at left
    with dissolve
    narrador "Bem-vindos  a  Fonte  da  sorte,  um  lugar  mágico..." 
    show fontefinal movie
    with dissolve
    show narrador2 at left  
    with dissolve
    play sound "somFonte.mp3"
    narrador  "Um jardim que uma vez por ano se abre para aventureiros que desejam realizar seus desejos mais profundos"
    stop sound
    show cenario5
    with dissolve
    narrador "Essas 4 pessoas foram escolhidas para lutar pelo o uso da fonte, três bruxas e um cavaleiro, porém apenas um deles poderá fazer uso dos poderes da fonte"
    scene cenario6
    with dissolve
    show ana1 at right 
    with dissolve
    narrador " Esta é Ana, ela foi abandonada por um homem que ela amava profundamente, agora procura a cura do seu coração partido e da saudade."
    scene cenario6
    with dissolve
    show amanda1 at left
    with dissolve
    narrador "Esta é Amanda, ela teve seu ouro e sua varinha roubados por um bruxo malvado"
    scene cenario6
    with dissolve
    show maria1 
    with dissolve
    narrador "Esta é Maria, uma senhora doente a procura de um alivio para suas fortes dores"
    scene cenario6
    with dissolve
    show cavaleiro1 at right
    with dissolve
    narrador "Este é Davi, um cavaleiro azarado procurando coragem e sucesso"
    show portal movie
    play sound "somPortal.mp3"
    with dissolve
    narrador "O portal esta se abrindo para que os viajantes tentem chegar até forte da sorte"
    stop sound
    scene fundofloresta
    play sound "somFloresta.mp3"
    $ renpy.movie_cutscene("entrada.mpg")
    stop sound
    with dissolve
    scene fundofloresta
    with dissolve
    show mariaespelhada at right
    with dissolve
    maria "Não entendo o motivo de um simples cavaleiro ter sido escolhido para entrar no jardim, por que motivo um ser não mágico poderia acessar uma fonte de imenso poder?"
    scene fundofloresta
    with dissolve
    show cavaleiro1 at left
    with dissolve
    menu:
        "Como assim? Pois saiba que sou tão digno quanto vocês":
            scene fundofloresta
            show cavaleiroraiva
            pause(1.0)
        "Creio que tem razão, pois sou apenas um cavaleiro e nao tenho capacidade de competir com a sua magia":
            scene fundofloresta
            show cavaleirosad
            pause(1.0)
    scene cenario6
    show mariaraiva at left
    with dissolve
    maria "Não tens coragem! Sinto que é um cavaleiro covarde e incapaz de triunfar em qualquer que seja sua missão."
    scene cenario6
    show amanda1 at right
    amanda "Podes ser um cavaleiro covarde, mas sinto que tens honra e um coração puro. E essas são as virtudes que todos os seres deveriam ter."
    scene cenario6
    show ana2 
    with dissolve
    ana "Já que você já está aqui dentro, tente ao menos não atrapalhar e nos ajude a conquistar o
nosso objetivo, vamos, temos um longo caminho pela frente!"
    play sound "somPassos.mp3"
    $ renpy.movie_cutscene("desafio.mpg")
    stop sound
    scene fundofloresta
    show estatua1 at right 
    with dissolve
    estatua"Paga-me com suas dores, bem-vindos ao seu primeiro desafio, nesse desafio um serão
escolhidas para se enfrentar essa criatura mágica"
    "Escolha um para o combate!"
    show escolha1
    menu:
        "Ana":
            $ anavida = True
            scene cenario7
            show ana3 at right
            show monstro at left
            ana"Irei derrotar essa fera e iremos conseguir prosseguir!"
            play sound "somFeitico.mp3"
            $ renpy.movie_cutscene("anabruxa.mpg")
            stop sound
            
            scene cenario7
            show anamorta
            with dissolve
            "O  monstro  absorve  o  feitiço,  ele revida jogando uma maldição que joga Ana no chão"
            "Sem forças, Ana não resiste a maldição e morre"
            scene cenario7
            play sound "somChoroHomem.mp3"
            show cavaleirochora at left
           
            stop sound
            with dissolve
            "O cavaleiro desolado com a morte de Ana, chora sentindo a dor da sua perda"
            scene cenario7
            show estatua1 at right
            with dissolve 
            estatua"Nesse desafio requer que um dos participantes sofra e que me pague com esse sofrimento,
vocês passaram e estão prontos para o próximo desafio"
            "Hora de prosseguir!"
            play sound "somPassos.mp3"
            $ renpy.movie_cutscene("semana.mpg")
            stop sound      
        
        
        "Maria":
            scene cenario7
            show maria3 at right
            show monstro at left
            maria"Irei derrotar essa fera e iremos conseguir prosseguir!"
            play sound "somFeitico.mp3"
            $ renpy.movie_cutscene("mariabruxa.mpg")
            stop sound
            show mariamorta
            "O  monstro  absorve  o  feitiço,  ele revida jogando uma maldição transformando a fisionomia de Maria que cai no chão"
            "Sem forças, Maria não resiste a maldição e morre"
            scene cenario7
            play sound "somChoroHomem.mp3"
            show cavaleirochora at left
            stop sound
            with dissolve
            "O cavaleiro desolado com a morte de Maria, chora sentindo a dor da sua perda"
            scene cenario7
            show estatua1 at right
            with dissolve 
            estatua"Nesse desafio requer que um dos participantes sofra e que me pague com esse sofrimento,
vocês passaram e estão prontos para o próximo desafio"
            play sound "Sompassos.mp3"
            $ renpy.movie_cutscene("semmaria.mpg")
            stop sound
            $ mariavida = True       
            
        
        
        "Amanda":
            scene cenario7
            show amanda2 at right
            show monstro at left
            amanda"Irei derrotar essa fera e iremos conseguir prosseguir!"
            play sound "somFeitico.mp3"
            $ renpy.movie_cutscene("amandabruxa.mpg")
            stop sound
            show amandamorta
            "O  monstro  absorve  o  feitiço,  ele revida jogando uma maldição que joga Amanda no chão"
            "Sem forças, Amanda não resiste a maldição e morre"
            scene cenario7
            play sound "somChoroHomem.mp3"
            show cavaleirochora at left
            with dissolve 
            stop sound
            "O cavaleiro desolado com a morte de Amanda, chora sentindo a dor da sua perda"
            scene cenario7
            show estatua1 at right
            with dissolve 
            estatua"Nesse desafio requer que um dos participantes sofra e que me pague com esse sofrimento,
vocês passaram e estão prontos para o próximo desafio"
            "Hora de prosseguir!"
            play sound "somPassos.mp3"
            $ renpy.movie_cutscene("semamanda.mpg")
            stop sound
            $amandavida = True
            
        "Davi":
            scene cenario7
            show cavaleiro1 at right
            show monstro at left
            amanda"Irei derrotar essa fera e iremos conseguir prosseguir!"
            $ renpy.movie_cutscene("davimorre.mpg")
            show davimorto
            "Antes de conseguir pegar sua espada para enfrentar a criatura, Davi é atigindo com um feitiço que o transforma e tira suas forças"
            "Sem forças, Davi não resiste a maldição e morre"
            play sound "somChoro.mp3"
            scene cenario7
            show amandachora at left
            stop sound
            with dissolve
            "Amanda desolada com a morte do Cavaleiro, chora sentindo a dor da sua perda"
            scene cenario7
            show estatua1 at right
            with dissolve 
            estatua"Nesse desafio requer que um dos participantes sofra e que me pague com esse sofrimento,
vocês passaram e estão prontos para o próximo desafio"
            play sound "somPassos.mp3"
            $ renpy.movie_cutscene("semdavi.mpg")
            stop sound 
            $ davivida = True
            scene lago
    scene cenario7
    show estatua1 at right
    with dissolve
    estatua"Pague-me com o suor do seu trabalho. Bem-vindos ao segundo desafio, nesse desafio um
dos participantes precisa resgatar uma pequena jóia que está no fundo desse lago."
if anavida:
    scene escolha2
    menu:
        "Maria":
            scene lago2
            show maria3 at left
            with dissolve
            scene lago2
            maria"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("mariamorta2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Maria para o fundo, ela tenta escapar, mas sem forças ela acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Maria me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
    terceiro e último desafio"
            $ mariavida =True
        "Amanda":
            scene lago2
            show amanda1 at left
            with dissolve
            scene lago2
            amanda"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("amandamorta2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Amanda para o fundo, ela tenta escapar, mas sem forças ela acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Amanda me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
    terceiro e último desafio"
            $ amandavida = True
        "Davi":
            scene lago2
            show cavaleiro1 at left
            with dissolve
            scene lago2
            cavaleiro"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("davimorto2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Davi para o fundo, ele tenta escapar, mas sem forças ele acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Davi me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
    terceiro e último desafio"
            $ davivida = True
    
elif mariavida:
    scene escolha22
    menu:
        "Ana":
            scene lago2
            show ana2 at left
            with dissolve
            scene lago2
            ana"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $renpy.movie_cutscene("anamorta2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Ana para o fundo, ela tenta escapar, mas sem forças ela acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Ana me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
        terceiro e último desafio"
            $ anavida = True
        "Amanda":  
            scene lago2
            show amanda1 at left
            with dissolve
            scene lago2
            amanda"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("amandamorta2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Amanda para o fundo, ela tenta escapar, mas sem forças ela acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Amanda me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
        terceiro e último desafio"
            $ amandavida = True
        "Davi":
            scene lago2
            show cavaleiro1 at left
            with dissolve
            scene lago2
            cavaleiro"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("davimorto2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Davi para o fundo, ele tenta escapar, mas sem forças ele acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Davi me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
        terceiro e último desafio"
            $ davivida = True
        
elif amandavida:
    scene escolha23
    menu:
        "Ana":
            scene lago2
            show ana2 at left
            with dissolve
            scene lago2
            ana"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("anamorta2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Ana para o fundo, ela tenta escapar, mas sem forças ela acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Ana me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
    terceiro e último desafio"
            $ anavida = True
        "Maria":
            scene lago2
            show maria3 at left
            with dissolve
            scene lago2
            maria"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("mariamorta2.mpg")
            stop sound
            "“Existe um feitiço no lago que puxa Maria para o fundo, ela tenta escapar, mas sem forças ela acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Maria me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
        terceiro e último desafio"
            $ mariavida = True
        "Davi":
            scene lago2
            show cavaleiro1 at left
            with dissolve
            scene lago2
            cavaleiro"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("davimorto2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Davi para o fundo, ele tenta escapar, mas sem forças ele acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Davi me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
        terceiro e último desafio"
            $ davivida = True
        
elif davivida:
    scene escolha24
    menu:
        "Ana":
            scene lago2
            show ana2 at left
            with dissolve
            scene lago2
            ana"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("anamorta2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Ana para o fundo, ela tenta escapar, mas sem forças ela acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Ana me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
            terceiro e último desafio"
            $ anavida= True
        "Maria":
            scene lago2
            show maria3 at left
            with dissolve
            scene lago2
            maria"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("mariamorta2.mpg")
            stop sound
            "Existe um feitiço no lago que puxa Maria para o fundo, ela tenta escapar, mas sem forças ela acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Maria me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
            terceiro e último desafio"
            $ mariavida = True
        "Amanda":
            scene lago2
            show amanda1 at left
            with dissolve
            scene lago2
            amanda"Eu irei resgatar a jóia para continuar nossa jornada!"
            play sound "somBoiando.wav"
            $ renpy.movie_cutscene("amandamorta2.mpg")
            stop sound
            "“Existe um feitiço no lago que puxa Amanda para o fundo, ela tenta escapar, mas sem forças ela acaba não resistindo ao lago"
            show estatua1 at right 
            estatua"Amanda me pagou com o suor do seu trabalho, por seu sacrifício vocês estão prontos para o
            terceiro e último desafio"
            $ amandavida= True
    
#TERCEIRO DESAFIO
scene fundofloresta
show estatua1 at left
estatua"Pague-me com uma lembrança valiosa. Bem-vindos ao último desafio, nesse desafio um
dos participantes tem que abdicar de uma memória escolhida por mim."
if anavida and mariavida:
    scene escolhafinal
    menu:
        "Amanda":
            scene fundofloresta
            show estatua1
            estatua"Amanda foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto ao seus companheiros de jornada."
            scene fundofloresta
            estatua"Amanda esquecerá do momento em que conheceu Davi, porque a existência de
Davi será apagada desse mundo"
            
            $ renpy.movie_cutscene("davi_desaparece.mpg")
            show estatua1 at right
            estatua"Amanda, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show amanda1 
            amanda"Eu fui roubada por um bruxo do mal, e desejo as minhas posses de volta"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("amandavenceu.mpg")
            stop sound 
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
        
        "Davi":
            scene fundofloresta
            show estatua1
            estatua"Davi foi o escolhido para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            estatua"Davi esquecerá do momento em que conheceu Amanda, porque a existência da
Amanda será apagada desse mundo"
            $ renpy.movie_cutscene("amanda_desaparece.mpg")
            scene fundofloresta
            show estatua1
            estatua"Davi, você foi digno e passou por todos os desafios e armadilhas que lhe foram
impostas, você é o vitorioso que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound 
            scene fundofloresta
            show cavaleiro1
            cavaleiro"Eu desejo força e coragem, quero ser um cavaleiro bem sucedido"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("davivence.mpg")
            stop sound
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
elif anavida and davivida:
    scene escolhafinal2
    menu:
        
        "Amanda":
            scene fundofloresta
            show estatua1
            estatua"Amanda foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto ao seus companheiros de jornada."
            estatua"Amanda esquecerá do momento em que conheceu Maria, porque a existência de
Maria será apagada desse mundo"
            $ renpy.movie_cutscene("maria_desaparece.mpg")
            scene fundofloresta
            show estatua1
            estatua"Amanda, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show amanda1
            amanda"Eu fui roubada por um bruxo do mal, e desejo as minhas posses de volta"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("amandavenceu.mpg")
            stop sound
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
        "Maria":
            scene fundofloresta
            show estatua1
            estatua"Maria foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            show estatua1 at right
            with dissolve
            estatua"Maria esquecerá do momento em que conheceu Amanda, porque a existência de
Amanda será apagada desse mundo"
            $ renpy.movie_cutscene("amanda_desaparece.mpg")
            show estatua1 at right
            with dissolve
            estatua"Maria, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show maria3
            with dissolve
            maria"“Eu desejo alívio para as minhas dores, sou uma velha doente e quero minha saúde de
volta."
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("mariavenceu.mpg")
            stop sound
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
        
elif anavida and amandavida:
    scene escolhafinal3
    menu:
        "Davi":
            scene fundofloresta
            show estatua1
            estatua "Davi foi o escolhido para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            show estatua1
            estatua"Davi esquecerá do momento em que conheceu Maria, porque a existência de
Maria será apagada desse mundo"
            $ renpy.movie_cutscene("maria_desaparece.mpg")
            show estatua1
            estatua"Davi, você foi digno e passou por todos os desafios e armadilhas que lhe foram
impostas, você é o vitorioso que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show cavaleiro1
            cavaleiro"Eu desejo força e coragem, quero ser um cavaleiro bem sucedido"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("davivence.mpg")
            stop sound
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
        "Maria":
            scene fundofloresta
            show estatua1
            estatua"Maria foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto ao seus companheiros de jornada."
            scene fundofloresta
            show estatua1 at right
            estatua"Maria esquecerá do momento em que conheceu Davi, porque a existência de
Davi será apagada desse mundo"
            $ renpy.movie_cutscene("davi_desaparece.mpg")
            show estatua1 at right
            estatua"Maria, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show maria3
            maria"“Eu desejo alívio para as minhas dores, sou uma velha doente e quero minha saúde de
volta."
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("mariavenceu.mpg")
            stop sound
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
        
elif amandavida and mariavida:
    scene escolhafinal12
    menu:
        "Ana":
            scene fundofloresta
            show estatua1
            estatua"Ana foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto ao seus companheiros de jornada."
            scene fundofloresta
            show estatua1 at right
            estatua"Ana esquecerá do momento em que conheceu Davi, porque a existência de
Davi será apagada desse mundo"
            $ renpy.movie_cutscene("davi_desaparece.mpg")
            show estatua1 at right
            estatua"Ana, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            play sound "somFonte.mp3"
            scene fundofloresta
            show ana1
            with dissolve
            ana"Eu fui abandonada por um homem que eu amava muito. Desejo alívio para a minha
saudade"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("anavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
        
        "Davi":
            scene fundofloresta
            show estatua1
            estatua"Davi foi o escolhido para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Davi esquecerá do momento em que conheceu Ana, porque a existência de
Ana será apagada desse mundo"
            $ renpy.movie_cutscene("ana_desaparece.mpg")
            show estatua1 at right
            estatua"Davi, você foi digno e passou por todos os desafios e armadilhas que lhe foram
impostas, você é o vitorioso que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show cavaleiro1
            cavaleiro"Eu desejo força e coragem, quero ser um cavaleiro bem sucedido"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("davivence.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
elif amandavida and davivida:
    
    scene escolhafinal13
    menu:
        "Ana":
            scene fundofloresta
            show estatua1
            estatua"Ana foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Ana esquecerá do momento em que conheceu Maria, porque a existência de
Maria será apagada desse mundo"
            $ renpy.movie_cutscene("maria_desaparece.mpg")
            
            estatua"Ana, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show ana1
            ana"Eu fui abandonada por um homem que eu amava muito. Desejo alívio para a minha
saudade"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("anavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
    
        "Maria":
        
            scene fundofloresta
            show estatua1
            estatua"Maria foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Maria esquecerá do momento em que conheceu Ana, porque a existência de
Ana será apagada desse mundo"
            $ renpy.movie_cutscene("ana_desaparece.mpg")
            
            estatua"Maria, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show maria3
            maria"“Eu desejo alívio para as minhas dores, sou uma velha doente e quero minha saúde de
volta."
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("mariavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
        
elif amandavida and anavida:
    scene escolhafinal3
    menu:
        "Davi":
            scene fundofloresta
            show estatua1
            estatua"Davi foi o escolhido para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Davi esquecerá do momento em que conheceu Maria, porque a existência de
Maria será apagada desse mundo"
            $ renpy.movie_cutscene("maria_desaparece.mpg")
            
            
            estatua"Davi, você foi digno e passou por todos os desafios e armadilhas que lhe foram
impostas, você é o vitorioso que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show cavaleiro1
            cavaleiro"Eu desejo força e coragem, quero ser um cavaleiro bem sucedido"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("davivence.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
        "Maria":
            scene fundofloresta
            show estatua1
            estatua"Maria foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Maria esquecerá do momento em que conheceu Davi, porque a existência de
Davi será apagada desse mundo"
            $ renpy.movie_cutscene("davi_desaparece.mpg")
            estatua"Maria, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show maria3
            maria"“Eu desejo alívio para as minhas dores, sou uma velha doente e quero minha saúde de
volta."
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("mariavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            narrador"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
elif mariavida and anavida:
    scene escolhafinal14
    
    menu:
        "Davi":
            scene fundofloresta
            show estatua1
            estatua"Davi foi o escolhido para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Davi esquecerá do momento em que conheceu Amanda, porque a existência de
Amanda será apagada desse mundo"
            $ renpy.movie_cutscene("amanda_desaparece.mpg")
            
            estatua"Davi, você foi digno e passou por todos os desafios e armadilhas que lhe foram
impostas, você é o vitorioso que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show cavaleiro1
            cavaleiro"Eu desejo força e coragem, quero ser um cavaleiro bem sucedido"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("davivence.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
        "Amanda":
            scene fundofloresta
            show estatua1
            estatua"Amanda foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Amanda esquecerá do momento em que conheceu Davi, porque a existência de
Davi será apagada desse mundo"
            $ renpy.movie_cutscene("davi_desaparece.mpg")
            estatua"Amanda, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound 
            scene fundofloresta
            show amanda1
            amanda"Eu fui roubada por um bruxo do mal, e desejo as minhas posses de volta"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("amandavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
            
elif mariavida and davivida:
    scene escolhafinal15
    menu:
        "Amanda":
            scene fundofloresta
            show estatua1
            estatua"Amanda foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Amanda esquecerá do momento em que conheceu Ana, porque a existência de
Ana será apagada desse mundo"
            $ renpy.movie_cutscene("ana_desaparece.mpg")
            estatua"Amanda, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show amanda1
            amanda"Eu fui roubada por um bruxo do mal, e desejo as minhas posses de volta"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("amandavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
        "Ana":
            scene fundofloresta
            show estatua1
            estatua"Ana foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Ana esquecerá do momento em que conheceu Amanda, porque a existência de
Amanda será apagada desse mundo"
            $ renpy.movie_cutscene("amanda_desaparece.mpg")
            
            estatua"Ana, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show ana1
            ana"Eu fui roubada por um bruxo do mal, e desejo as minhas posses de volta"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("anavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
elif mariavida and amandavida:
    scene escolhafinal12
    menu:
        "Ana":
            
            scene fundofloresta
            show estatua1
            estatua"Ana foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Ana esquecerá do momento em que conheceu Davi, porque a existência de
Davi será apagada desse mundo"
            $ renpy.movie_cutscene("davi_desaparece.mpg")
            estatua"Ana, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show ana1
            ana"Eu fui abandonada por um homem que eu amava muito. Desejo alívio para a minha
saudade"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("anavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
        "Davi":
            scene fundofloresta
            show estatua1
            estatua"Davi foi o escolhido para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Davi esquecerá do momento em que conheceu Ana, porque a existência de
Ana será apagada desse mundo"
            $ renpy.movie_cutscene("ana_desaparece.mpg")
            
            estatua"Davi, você foi digno e passou por todos os desafios e armadilhas que lhe foram
impostas, você é o vitorioso que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show cavaleiro1
            cavaleiro"Eu desejo força e coragem, quero ser um cavaleiro bem sucedido"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("davivence.mpg")         
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
            
elif davivida and anavida:
    scene escolhafinal2
    menu:
        "Amanda":
            scene fundofloresta
            show estatua1
            estatua"Amanda foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Amanda esquecerá do momento em que conheceu Maria, porque a existência de
Maria será apagada desse mundo"
            $ renpy.movie_cutscene("maria_desaparece.mpg")
            estatua"Amanda, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show amanda1
            amanda"Eu fui roubada por um bruxo do mal, e desejo as minhas posses de volta"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("amandavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
            
        "Maria":
            scene fundofloresta
            show estatua1
            estatua"Maria foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Maria esquecerá do momento em que conheceu Amanda, porque a existência de
Amanda será apagada desse mundo"
            $ renpy.movie_cutscene("amanda_desaparece.mpg")
            estatua"Maria, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show maria3
            maria"“Eu desejo alívio para as minhas dores, sou uma velha doente e quero minha saúde de
volta."
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("mariavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"

elif davivida and mariavida:
    scene escolhafinal15
    menu:
        "Ana":
            scene fundofloresta
            show estatua1
            estatua"Ana foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Ana esquecerá do momento em que conheceu Amanda, porque a existência de
Amanda será apagada desse mundo"
            $ renpy.movie_cutscene("amanda_desaparece.mpg")
            
            estatua"Ana, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show ana1
            ana"Eu fui abandonada por um homem que eu amava muito. Desejo alívio para a minha
saudade"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("anavenceu.mpg")
            stop sound
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
        "Amanda":
            scene fundofloresta
            show estatua1
            estatua"Amanda foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Amanda esquecerá do momento em que conheceu Ana, porque a existência de
Ana será apagada desse mundo"
            $ renpy.movie_cutscene("ana_desaparece.mpg")
            estatua"Amanda, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound 
            scene fundofloresta
            show amanda1
            amanda"Eu fui roubada por um bruxo do mal, e desejo as minhas posses de volta"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("amandavenceu.mpg")
            stop sound 
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"

elif davivida and amandavida:
    scene escolhafinal13
    menu:
        "Ana":
            scene fundofloresta
            show estatua1
            estatua"Ana foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Ana esquecerá do momento em que conheceu Maria, porque a existência de
Maria será apagada desse mundo"
            $ renpy.movie_cutscene("maria_desaparece.mpg")
            
            estatua"Ana, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound
            scene fundofloresta
            show ana1
            ana"Eu fui abandonada por um homem que eu amava muito. Desejo alívio para a minha
saudade"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("anavenceu.mpg")
            stop sound 
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
        "Maria":
            scene fundofloresta
            show estatua1
            estatua"Maria foi a escolhida para perder uma memória. Essa memória será do exato
momento em que entrou no portal junto às suas companheiras de jornada."
            scene fundofloresta
            estatua"Maria esquecerá do momento em que conheceu Ana, porque a existência de
Ana será apagada desse mundo"
            $ renpy.movie_cutscene("ana_desaparece.mpg")
            show estatua at right
            estatua"Maria, você foi digna e passou por todos os desafios e armadilhas que lhe foram
impostas, você é a vitoriosa que poderá ter um desejo realizado pela fonte da sorte"
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("fontefinal.mpg")
            stop sound 
            scene fundofloresta
            show maria3
            maria"“Eu desejo alívio para as minhas dores, sou uma velha doente e quero minha saúde de
volta."
            play sound "somFonte.mp3"
            $ renpy.movie_cutscene("mariavenceu.mpg")
            stop sound 
            scene fundofloresta
            show estatua1 at right
            estatua"Essa foi a história da fonte da sorte e dos sacrifícios que as diversas criaturas fazem
por ela. O que se perde tentando realizar um desejo?"
            
        # tem que colocar um video da floresta com os personagens 
        
        
        # This ends the game.
return
       
