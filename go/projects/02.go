package main

import (
	"image/color"

	"github.com/hajimehoshi/ebiten/v2"
	"github.com/hajimehoshi/ebiten/v2/ebitenutil"
)

type Game struct {
	x, y float64
}

func (g *Game) Update() error {
	if ebiten.IsKeyPressed(ebiten.KeyArrowLeft) {
		g.x -= 5
	}
	if ebiten.IsKeyPressed(ebiten.KeyArrowRight) {
		g.x += 5
	}
	if ebiten.IsKeyPressed(ebiten.KeyArrowUp) {
		g.y -= 5
	}
	if ebiten.IsKeyPressed(ebiten.KeyArrowDown) {
		g.y += 5
	}
	return nil
}

func (g *Game) Draw(screen *ebiten.Image) {
	ebitenutil.DrawRect(screen, g.x, g.y, 50, 50, color.RGBA{255, 0, 0, 255})
}

func (g *Game) Layout(outsideWidth, outsideHeight int) (int, int) {
	return 800, 600
}

func main() {
	game := &Game{x: 400, y: 300}
	ebiten.RunGame(game)
}
