# main.py
import storage as st
import models as m
import operations as op

def main():
    storage = st.Storage("holiday_state.json")
    holiday = m.Holiday("Без названия", "Planned")
    cli = op.CLI(holiday, storage)
    cli.run()

if __name__ == "__main__":
    main()