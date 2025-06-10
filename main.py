from fastapi import FastAPI

app = FastAPI()


@app.get("/minecraft/how")
async def root():
    result = ("Итак, ты хочешь поиграть на моем сервачке. Как же это сделать? Все предельно просто:"
              "\n1 - тебе нужно поставить сборку 'Pokehaan Craft 2-2.10.0'"
              "\n2 - добавить сервер вот его адрес 'superznake.store:25565'"
              "\n3 - написать боту /launch, если сервер не запущен."
              "\nГотово."
              "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
              "\nP.S. Это сборка с покемонами, чтобы начать нужно выбрать себе стартового и подтвердить выбор")
    return result
