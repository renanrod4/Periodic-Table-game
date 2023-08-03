import pygame
from random import randint
from time import sleep
import time
import unicodedata
pygame.init()

#? VARS
display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
xwindow,ywindow = pygame.display.get_window_size()
pygame.display.set_caption("Jogo Tabela Periódica")
programIcon = pygame.image.load('./sprites/quimica-3279185159')

pygame.display.set_icon(programIcon)
gameloop = True
started = False
startgroup = pygame.sprite.Group()
drawgroup = pygame.sprite.Group()
losegroup = pygame.sprite.Group()
wingroup = pygame.sprite.Group()
tutorialgroup = pygame.sprite.Group()

font = pygame.font.SysFont(None, 240)
fontpoints = pygame.font.SysFont(None, 100)
fontdescript = pygame.font.SysFont(None, 40)

fontnames = pygame.font.SysFont(None, 80)


font_ans = pygame.font.SysFont(None, 60)
seconds = 0
points = 0
timer = 0

#? VARS WORDLIST
fonttitle = pygame.font.SysFont(None, 140)
siglas = ("H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Ai", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn", "Sb", "Te", "I", "Xe", "Cs", "Ba", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Ti", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds", "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb", "Lu", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm", "Md")
nomes = ("Hidrogênio", "Hélio", "Lítio", "Berílio", "Boro", "Carbono", "Nitrogênio", "Oxigênio", "Flúor", "Neônio", "Sódio", "Magnésio", "Alumínio", "Silício", "Fósforo", "Enxofre", "Cloro", "Argônio", "Potássio", "Cálcio", "Escândio", "Titânio", "Vanádio", "Cromo", "Manganês", "Ferro", "Cobalto", "Níquel", "Cobre", "Zinco", "Gálio", "Germânio", "Arsênio", "Selênio", "Bromo", "Criptônio", "Rubídio", "Estrôncio", "Ítrio", "Zircônio", "Nióbio", "Molibdênio", "Tecnécio", "Rutênio", "Ródio", "Paládio", "Prata", "Cádmio", "Índio", "Estanho", "Antimônio", "Telúrio", "Iodo", "Xenônio", "Césio", "Bário", "Háfnio", "Tântalo", "Tungstênio", "Rênio", "Ósmio", "Irídio", "Platina", "Ouro", "Mercúrio", "Tálio", "Chumbo", "Bismuto", "Polônio", "Ástato", "Radônio", "Frâncio", "Rádio", "Rutherfórdio", "Dúbnio", "Seabórgio", "Bóhrio", "Hássio", "Meitnério", "Darmstádtio", "Roentgênio", "Copernício", "Nihônio", "Fleróvio", "Moscóvio", "Livermório", "Tenesso", "Oganessônio", "Lantânio", "Cério", "Praseodímio", "Neodímio", "Promécio", "Samário", "Európio", "Gadolínio", "Térbio", "Disprósio", "Hólmio", "Érbio", "Túlio", "Itérbio", "Lutécio", "Actínio", "Tório", "Protactínio", "Urânio", "Neptúnio", "Plutônio", "Amerício", "Cúrio", "Berquélio", "Califórnio", "Einstênio", "Férmio", "Mendelévio")
randelement = randint(1,110)
siglasorteada = siglas[randelement]
nomesorteado = nomes[randelement]
#? VARS INPUT
inputresposta = ""
inputrect = pygame.Rect(xwindow/2-245,ywindow/2+270,490,60)
colorinputrect = pygame.Color(("#2a2f39"))
respdigits= 0
correct = False
respondido = False
wrong = False
initime = time.time()
lose = False
win = False
lasttime = 0
first_check = False
#? VARS TUTORIAL

tutorialrect = pygame.Rect(xwindow/2-750,ywindow/2-450,1500,900)
creditrect = pygame.Rect(xwindow/2-750,ywindow/2-450,1500,900)

isintutorial = False
isincredits = False


#? BACKGROUND CONFIG
background = pygame.sprite.Sprite(startgroup)
background.image = pygame.image.load("./sprites/hydrocortisone.png")
background.image = pygame.transform.scale(background.image,[xwindow,ywindow])
background.rect = pygame.Rect(0,0,xwindow,ywindow)

gameover = pygame.sprite.Sprite(losegroup)
gameover.image = pygame.image.load("./sprites/image.png")
gameover.image = pygame.transform.scale(gameover.image,[600,309])
gameover.rect = pygame.Rect(xwindow/2-300,ywindow/2-154,600,309)

gamewin = pygame.sprite.Sprite(wingroup)
gamewin.image = pygame.image.load("./sprites/imagewin.png")
gamewin.image = pygame.transform.scale(gamewin.image,[791,566])
gamewin.rect = pygame.Rect(xwindow/2-395,ywindow/2-283,791,566)




#? BUTTON CONFIG
button = pygame.sprite.Sprite(startgroup)
button.image = pygame.image.load("./sprites/5261565.png")
button.image = pygame.transform.scale(button.image,[256,129])
button.rect = pygame.Rect(xwindow/2-(256/2),ywindow-300,256,129)

tutorial = pygame.sprite.Sprite(startgroup)
tutorial.image = pygame.image.load("./sprites/TUTORIALBUTTON.png")
tutorial.image = pygame.transform.scale(tutorial.image,[256,129])
tutorial.rect = pygame.Rect(xwindow/2-(256/2)-270,ywindow-300,256,129)



credit = pygame.sprite.Sprite(startgroup)
credit.image = pygame.image.load("./sprites/CREDITBUTTON.png")
credit.image = pygame.transform.scale(credit.image,[256,129])
credit.rect = pygame.Rect(xwindow/2-(256/2)+270,ywindow-300,256,129)
# Cores
COR_FUNDO_VITORIA = (152, 195, 121)  # Verde esmeralda
COR_FUNDO_DERROTA = (224, 107, 116)  # Vermelho claro

COR_TEXTO = (236, 240, 241)        # Branco

#? FUNCTIONS 

def restart_game():
    global started, correct, wrong, lose, win, respondido, inputresposta, respdigits, points, initime
    started = False
    correct = False
    wrong = False
    lose = False
    win = False
    respondido = False
    inputresposta = ""
    respdigits = 0
    points = 0
    initime = time.time()


def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto) if unicodedata.category(c) != 'Mn')

def verify(answer,correctanswer):
    if str(answer).lower() == str(correctanswer).lower():
        print("acertou :)")
        display.fill([0, 255, 0])
    answer_sem_acento = remover_acentos(str(answer))
    correct_sem_acento = remover_acentos(str(correctanswer))
    
    print(answer_sem_acento.lower())
    print(correctanswer.lower())
    return answer_sem_acento.lower() == correct_sem_acento.lower()

def show_win_message():
    display.fill(COR_FUNDO_VITORIA)  # Cor verde para vitória
    win_text = fonttitle.render("Você venceu!", True, ("#000000"))
    text_rect = win_text.get_rect(center=(xwindow/2, ywindow/2))
    display.blit(win_text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)  # Aguarde 2 segundos antes de reiniciar

def show_lose_message():
    display.fill(COR_FUNDO_DERROTA)  # Cor vermelha para derrota
    lose_text = fonttitle.render("Você perdeu!", True, ("#000000"))
    text_rect = lose_text.get_rect(center=(xwindow/2, ywindow/2))
    display.blit(lose_text, text_rect)
    pygame.display.update()
    pygame.time.wait(2000)  # Aguarde 2 segundos antes de reiniciar


#? GAME
while gameloop:
    
    if started == False or isintutorial or isincredits:
        initime = time.time()
    if correct == False and wrong == False and lose == False and win == False:
        display.fill("#2f3440")
    
    if correct == True and wrong == False and lose == False and win == False:
        
        display.fill("#a2bd8c")

    if correct == False and wrong == True and lose == False and win == False:
        display.fill("#BF616A")
    if win == True:
        display.fill("#00ff00")
        wingroup.draw(display)
        show_win_message()
        restart_game()

    if lose == True:
        display.fill("#ff0000")
        losegroup.draw(display)
        show_lose_message()
        restart_game()

    if not started and not isintutorial and not isincredits:
        startgroup.draw(display)
    else:
        drawgroup.draw(display)

    if isintutorial:
        pygame.draw.rect(display,"#292E39",tutorialrect)
        
    if isincredits:
        pygame.draw.rect(display,"#292E39",creditrect)
    

    if started == True:
        if win == True or lose == True:
            timer = 0
        else:
            timer = seconds-initime
        imgsigla = font.render(str(siglasorteada), True, ("#D8DEE9"))
        text_rect = imgsigla.get_rect(center=(xwindow/2, ywindow/2-100))
        display.blit(imgsigla, text_rect)

        if timer < 15:
            timer = font.render(str(round(20-timer)), True, ("#D8DEE9"))
        else:
            timer = font.render(str(round(20-timer)), True, ("#cf8770"))


        timer_rect = timer.get_rect(center=(xwindow/2, 100))
        display.blit(timer, timer_rect)

        pointscount = fontpoints.render(str(round(points)), True, ("#D8DEE9"))
        points_rect = pointscount.get_rect(center=(xwindow-200, 100))
        display.blit(pointscount, points_rect)

        pygame.draw.rect(display,colorinputrect,inputrect)
        imgnome = font_ans.render(str(inputresposta), True, ("#D8DEE9"))
        text_rectname = imgnome.get_rect(center=(xwindow/2, ywindow/2+300))
        display.blit(imgnome, text_rectname)
        seconds = time.time()
        if points >= 5:
            win = True
            show_win_message()
            restart_game()

        if round(seconds - initime) > 20:
            lose = True
            show_lose_message()
            restart_game()




    else:
        if started == False and isintutorial == False and not isincredits:
            title = fonttitle.render("Jogo Da Tabela Periódica", True, ("#D8DEE9"))
            text_title = title.get_rect(center=(xwindow/2, ywindow/2-300))
            display.blit(title, text_title)
        
        if isintutorial:
            tutorialtitle = fonttitle.render("Como jogar", True, ("#88C0D0"))
            text_tutorialtitle = tutorialtitle.get_rect(center=(xwindow/2, ywindow/2-300))
            display.blit(tutorialtitle, text_tutorialtitle)

            tutorialdescrip = fontdescript.render("""Quando começar a jogar voce verá que tem um timer de 20 segundos, quando o timer chegar a 0 você perde.""", True, ("#D8DEE9"))
            text_tutorialdescrip = tutorialdescrip.get_rect(center=(xwindow/2, ywindow/2-200+200))
            display.blit(tutorialdescrip, text_tutorialdescrip)
            tutorialdescrip2 = fontdescript.render("""Aparecerá aleatoriamente siglas da tabela periódica, seu objetivo é dizer quais são os elementos""", True, ("#D8DEE9"))
            text_tutorialdescrip2 = tutorialdescrip2.get_rect(center=(xwindow/2, ywindow/2-175+200))
            display.blit(tutorialdescrip2, text_tutorialdescrip2)
            tutorialdescrip3 = fontdescript.render("""referentes as siglas, toda vez que voce acertar o timer é reiniciado, quando você acertar 5 elementos""", True, ("#D8DEE9"))
            text_tutorialdescrip3 = tutorialdescrip3.get_rect(center=(xwindow/2, ywindow/2-150+200))
            display.blit(tutorialdescrip3, text_tutorialdescrip3)
            tutorialdescrip4 = fontdescript.render("""você ganha.""", True, ("#D8DEE9"))
            text_tutorialdescrip4 = tutorialdescrip4.get_rect(center=(xwindow/2, ywindow/2-125+200))
            display.blit(tutorialdescrip4, text_tutorialdescrip4)

            exittutorial = fontdescript.render("""Clique fora da janela para fechar o Tutorial""", True, ("#4C566A"))
            text_exittutorial = exittutorial.get_rect(center=(xwindow/2, ywindow/2-125+500))
            display.blit(exittutorial, text_exittutorial)

        elif isincredits:
            creditstitle = fonttitle.render("Créditos", True, ("#88C0D0"))
            text_creditstitle = creditstitle.get_rect(center=(xwindow/2, ywindow/2-300))
            display.blit(creditstitle, text_creditstitle)

            tutorialdescrip = fontnames.render("Renan", True, ("#A3BE8C"))
            text_tutorialdescrip = tutorialdescrip.get_rect(center=(xwindow/2, ywindow/2-200))
            display.blit(tutorialdescrip, text_tutorialdescrip)

            tutorialdescrip = fontnames.render("Vinicius", True, ("#5E81AC"))
            text_tutorialdescrip = tutorialdescrip.get_rect(center=(xwindow/2, ywindow/2-200+50))
            display.blit(tutorialdescrip, text_tutorialdescrip)

            tutorialdescrip = fontnames.render("Nathan", True, ("#B48EAD"))
            text_tutorialdescrip = tutorialdescrip.get_rect(center=(xwindow/2, ywindow/2-200+100))
            display.blit(tutorialdescrip, text_tutorialdescrip)

            tutorialdescrip = fontnames.render("Roncatti", True, ("#BF616A"))
            text_tutorialdescrip = tutorialdescrip.get_rect(center=(xwindow/2, ywindow/2-200+150))
            display.blit(tutorialdescrip, text_tutorialdescrip)

            tutorialdescrip = fontnames.render("Pedro", True, ("#EBCB8B"))
            text_tutorialdescrip = tutorialdescrip.get_rect(center=(xwindow/2, ywindow/2-200+200))
            display.blit(tutorialdescrip, text_tutorialdescrip)

            tutorialdescrip = fontnames.render("Lucas", True, ("#D08770"))
            text_tutorialdescrip = tutorialdescrip.get_rect(center=(xwindow/2, ywindow/2-200+250))
            display.blit(tutorialdescrip, text_tutorialdescrip)
            exittutorial = fontdescript.render("""Clique fora da janela para fechar os créditos""", True, ("#4C566A"))
            text_exittutorial = exittutorial.get_rect(center=(xwindow/2, ywindow/2-125+500))
            display.blit(exittutorial, text_exittutorial)

    #? INPUTS
    if lose != "undefined":
        mouseposx,mouseposy = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameloop = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if mouseposx > xwindow/2-(248/2) and mouseposx < (xwindow/2-(248/2))+256 and mouseposy > ywindow-300 and mouseposy < ywindow-300+129 and isincredits == False and isintutorial == False:
                    started = True
                elif mouseposx > xwindow/2-(256/2)-270 and mouseposx < xwindow/2-(256/2)-270+256 and mouseposy > ywindow-300 and mouseposy < ywindow-300+129  and isincredits == False and started == False:                    
                    isintutorial = True
                if isintutorial == True:
                    if  not(mouseposx > xwindow/2-750 and mouseposx < xwindow/2-750+1500 and mouseposy > ywindow/2-450 and mouseposy < ywindow/2-450+900):
                        started = False
                        isintutorial = False
                        isincredits = False
                if isincredits:
                    if  not(mouseposx > xwindow/2-750 and mouseposx < xwindow/2-750+1500 and mouseposy > ywindow/2-450 and mouseposy < ywindow/2-450+900):
                        started = False
                        isincredits = False
                        isintutorial = False
                if mouseposx > xwindow/2-(256/2)+270 and mouseposx < xwindow/2-(256/2)+270+256 and mouseposy > ywindow-300 and mouseposy < ywindow-300+129 and isintutorial == False and started == False:                    
                    isincredits = True

            elif event.type == pygame.KEYDOWN:
                if respondido == False:    
                    if event.key == pygame.K_BACKSPACE:
                        if respdigits != 0:
                            inputresposta = inputresposta[:-1]
                            respdigits-=1
                    else:
                        if respdigits < 20:
                            inputresposta += event.unicode
                            if event.key != pygame.K_RETURN:
                                respdigits +=1
                if event.key == pygame.K_RETURN:
                    correct = verify(inputresposta,nomesorteado)
                    
                    inputresposta = inputresposta[0:-1]
                    if correct == True:
                        respondido = True
                    if remover_acentos(inputresposta.lower()) == remover_acentos(nomesorteado.lower()) :
                        correct = True
                        wrong = False
                        respdigits = 0
                        inputresposta = inputresposta[0:0]
                        randelement = randint(0,115)
                        siglasorteada = siglas[randelement]
                        nomesorteado = nomes[randelement]
                        initime = time.time()
                        points +=1
                        
                    else:
                        correct = False
                        wrong = True
                        inputresposta = inputresposta[0:0]
                        respdigits = 0


        keys = pygame.key.get_pressed()

    
    #? UPDATE
    pygame.display.update()
