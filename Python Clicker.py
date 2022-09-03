import pygame
import time
pygame.init()

WIDTH = 800
HEIGHT = 600
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
CASH = 0

BACKGROUND_COLOR = (0, 0, 0)
BUTTON_COLOR = (0, 255, 0)

FONT = pygame.font.SysFont('monospace', 15)

#Main Screen for drawing buttons
DRAW_SCREEN = pygame.Surface((WIDTH,HEIGHT))
DRAW_SCREEN.fill(BACKGROUND_COLOR)

#Buttons
MAINCLICK = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 50, 175, 30), 1)
GEN1 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 100, 200, 30), 1)
GEN12 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 135, 200, 30), 1)
GEN14 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 175, 200, 30), 1)
GEN16 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 225, 200, 30), 1)
GEN18 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 265, 200, 30), 1)
GEN2 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 315, 200, 30), 1)
GEN3 = pygame.draw.rect(DRAW_SCREEN, BUTTON_COLOR, pygame.Rect(0, 355, 200, 30), 1)

#Button Text
MAINCLICK_LABEL = FONT.render('Click for +1 Cash!', 1, (255, 255, 0))
GEN1_LABEL = FONT.render('10 for +5', 1, (255, 255, 0))
GEN12_LABEL = FONT.render('100 for +10', 1, (255, 255, 0))
GEN14_LABEL = FONT.render('100 for +10', 1, (255, 255, 0))
GEN16_LABEL = FONT.render('100 for +10', 1, (255, 255, 0))
GEN18_LABEL = FONT.render('100 for +10', 1, (255, 255, 0))
GEN2_LABEL = FONT.render('1000 for +100', 1, (255, 255, 0))
GEN3_LABEL = FONT.render('10000 for +1000', 1, (255, 255, 0))



#Profit Timers
GEN1_TIMER = 1100
GEN12_TIMER = 2100
GEN14_TIMER = 2600
GEN16_TIMER = 3100
GEN18_TIMER = 3600
GEN2_TIMER = 5100
GEN3_TIMER = 7600


#Generator Profits
MAINCLICK_PROFIT = 1
GEN1_PROFIT = 5
GEN12_PROFIT = 10
GEN14_PROFIT = 10
GEN16_PROFIT = 10
GEN18_PROFIT = 10
GEN2_PROFIT = 100
GEN3_PROFIT = 1000


#Generator Levels
GEN1_LEVEL = 0
GEN12_LEVEL = 0
GEN14_LEVEL = 0
GEN16_LEVEL = 0
GEN18_LEVEL = 0
GEN2_LEVEL = 0
GEN3_LEVEL = 0


#Generator Level Labels
GEN1_LEVEL_LABEL = 'Level: '
GEN12_LEVEL_LABEL = 'Level: '
GEN14_LEVEL_LABEL = 'Level: '
GEN16_LEVEL_LABEL = 'Level: '
GEN18_LEVEL_LABEL = 'Level: '
GEN2_LEVEL_LABEL = 'Level: '
GEN3_LEVEL_LABEL = 'Level: '


#Events
MAINCLICK_EVENT = pygame.USEREVENT + 1
GEN1_EVENT = pygame.USEREVENT + 2
GEN12_EVENT = pygame.USEREVENT + 3
GEN14_EVENT = pygame.USEREVENT + 4
GEN16_EVENT = pygame.USEREVENT + 5
GEN18_EVENT = pygame.USEREVENT + 5
GEN2_EVENT = pygame.USEREVENT + 6
GEN3_EVENT = pygame.USEREVENT + 9


def add_clicked_profit():
	global CASH
	CASH += MAINCLICK_PROFIT
	time.sleep(2)

def add_gen1_profit():
	global CASH
	CASH += GEN1_PROFIT
	
def add_gen12_profit():
	global CASH
	CASH += GEN12_PROFIT

def add_gen14_profit():
	global CASH
	CASH += GEN14_PROFIT

def add_gen16_profit():
	global CASH
	CASH += GEN16_PROFIT

def add_gen18_profit():
	global CASH
	CASH += GEN18_PROFIT

def add_gen2_profit():
	global CASH
	CASH += GEN2_PROFIT

def add_gen3_profit():
        global CASH
        CASH += GEN3_PROFIT


def handle_events():
	event_dict = {
	pygame.QUIT: exit,
	MAINCLICK_EVENT: add_clicked_profit,
	GEN1_EVENT: add_gen1_profit,
        GEN12_EVENT: add_gen12_profit,
        GEN14_EVENT: add_gen14_profit,
        GEN16_EVENT: add_gen16_profit,
        GEN18_EVENT: add_gen18_profit,
        GEN2_EVENT: add_gen2_profit,
        GEN3_EVENT: add_gen3_profit,
	}
	for event in pygame.event.get():
		if event.type in event_dict:
			event_dict[event.type]()

def handle_mouse_clicks():
	global CASH, PROFITS, GEN1_TIMER, GEN2_TIMER, GEN3_TIMER, GEN12_TIMER, GEN14_TIMER, GEN16_TIMER, GEN18_TIMER, GEN1_LEVEL, GEN2_LEVEL, GEN3_LEVEL, GEN4_LEVEL, GEN12_LEVEL, GEN14_LEVEL, GEN16_LEVEL, GEN18_LEVEL, GEN1_UP_LEVEL
	if pygame.mouse.get_focused():
		left_button = pygame.mouse.get_pressed()
		mouse_x, mouse_y = pygame.mouse.get_pos()
		if GEN1.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 10 and GEN1_TIMER > 100:
			CASH -= 10
			GEN1_TIMER -= 100
			pygame.time.set_timer(GEN1_EVENT, GEN1_TIMER)		
			GEN1_LEVEL += 1
		if GEN12.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 100 and GEN12_TIMER > 100:
			CASH -= 100
			GEN12_TIMER -= 100
			pygame.time.set_timer(GEN12_EVENT, GEN12_TIMER)		
			GEN12_LEVEL += 1
		if GEN14.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 100 and GEN14_TIMER > 100:
			CASH -= 100
			GEN14_TIMER -= 100
			pygame.time.set_timer(GEN14_EVENT, GEN14_TIMER)		
			GEN14_LEVEL += 1
		if GEN16.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 100 and GEN16_TIMER > 100:
			CASH -= 100
			GEN16_TIMER -= 100
			pygame.time.set_timer(GEN16_EVENT, GEN16_TIMER)		
			GEN16_LEVEL += 1
		if GEN18.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 100 and GEN18_TIMER > 100:
			CASH -= 100
			GEN18_TIMER -= 100
			pygame.time.set_timer(GEN18_EVENT, GEN18_TIMER)		
			GEN18_LEVEL += 1
		if GEN2.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 1000 and GEN2_TIMER > 100:
			CASH -= 1000
			GEN2_TIMER -= 100
			pygame.time.set_timer(GEN2_EVENT, GEN2_TIMER)
		if GEN3.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0) and CASH >= 10000 and GEN3_TIMER > 100:
			CASH -= 10000
			GEN3_TIMER -= 100
			pygame.time.set_timer(GEN3_EVENT, GEN3_TIMER)
			GEN3_LEVEL += 1
		if MAINCLICK.collidepoint(mouse_x, mouse_y) and left_button == (1,0,0):
			CASH += MAINCLICK_PROFIT
			time.sleep(0.5)
                        
def update_text():
	global CASH_LABEL, GEN1_LEVEL_LABEL, GEN12_LEVEL_LABEL, GEN14_LEVEL_LABEL, GEN16_LEVEL_LABEL, GEN18_LEVEL_LABEL, GEN2_LEVEL_LABEL, GEN3_LEVEL_LABEL, GEN1_UP_LEVEL_LABEL
	
	WINDOW.blit(DRAW_SCREEN, (0, 0))
	WINDOW.blit(GEN1_LABEL, (10, 108))
	WINDOW.blit(GEN12_LABEL, (10, 143))
	WINDOW.blit(GEN14_LABEL, (10, 183))
	WINDOW.blit(GEN16_LABEL, (10, 230))
	WINDOW.blit(GEN18_LABEL, (10, 273))
	WINDOW.blit(GEN2_LABEL, (10, 320))
	WINDOW.blit(GEN3_LABEL, (10, 365))
	WINDOW.blit(MAINCLICK_LABEL, (10, 54))
	CASH_LABEL = FONT.render('Total Cash: ${}'.format(CASH), 1, (255,255,0))
	WINDOW.blit(CASH_LABEL, (0, 0))
	GEN1_LEVEL_LABEL = FONT.render('Level: {}/{} --- $5/{} milliseconds'.format(GEN1_LEVEL, 10, GEN1_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN1_LEVEL_LABEL, (220, 108))
	GEN12_LEVEL_LABEL = FONT.render('Level: {}/{} --- $10/{} milliseconds'.format(GEN12_LEVEL, 20, GEN12_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN12_LEVEL_LABEL, (220, 143))
	GEN14_LEVEL_LABEL = FONT.render('Level: {}/{} --- $10/{} milliseconds'.format(GEN14_LEVEL, 25, GEN14_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN14_LEVEL_LABEL, (220, 188))
	GEN16_LEVEL_LABEL = FONT.render('Level: {}/{} --- $10/{} milliseconds'.format(GEN16_LEVEL, 30, GEN16_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN16_LEVEL_LABEL, (220, 233))
	GEN18_LEVEL_LABEL = FONT.render('Level: {}/{} --- $10/{} milliseconds'.format(GEN18_LEVEL, 35, GEN18_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN18_LEVEL_LABEL, (220, 278))
	GEN2_LEVEL_LABEL = FONT.render('Level: {}/{} --- $100/{} milliseconds'.format(GEN2_LEVEL, 50, GEN2_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN2_LEVEL_LABEL, (220, 323))
	GEN3_LEVEL_LABEL = FONT.render('Level: {}/{} --- $1000/{} milliseconds'.format(GEN3_LEVEL, 75, GEN3_TIMER), 1, (255,255,0))
	WINDOW.blit(GEN3_LEVEL_LABEL, (220, 368))
	pygame.display.flip()

def game_loop():
	while True:
		handle_events()
		handle_mouse_clicks()
		update_text()

def main():
	pygame.display.set_caption('Pythoniac Clicker')
	game_loop()

	
main()
