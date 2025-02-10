LOCAL = "LOCAL"     # Palabra especial para determinar el lenguaje de la maquina local.
TRANSLATORS = {}    # Diccionario de TRANSLATORS..
INTERPRETERS = {}   # Diccionario de interpretadores.
PROGRAMS = {}       # Diccionario de PROGRAMS.
MACHINES = []       # LIsta de maquinas creadas.

# Procedimiento que permite actualizar para todos los diccionarios en general, crearemos
# nuevos traductores, interpretes y maquinas de ser posible.
def GLOBAL_UPDATE():
    MACHINES.insert(0, LOCAL)
    for machine in MACHINES:
        if machine in INTERPRETERS:
            list_of_inter = INTERPRETERS[machine]
            for intr in list_of_inter:
                if MACHINES.count(intr) == 0:
                    MACHINES.extend(INTERPRETERS[machine])

        # Verificamos antes de continuar si no se generaon posibles traducores e interpretres.
        if machine in TRANSLATORS:
            NEW_TRANSLATOR(machine)
            IN_MACHINE_UPDATE(machine)
            for language in PROGRAMS.keys():
                if TRANSLATORS[machine].get(language) is not None:
                    for new_language in TRANSLATORS[machine][language]:
                        if "translated" not in PROGRAMS[language]:
                            PROGRAMS[language].update({"translated" : [[PROGRAMS[language]["initials"], new_language]]})
                        else:
                            for translates in PROGRAMS[language]["translated"]:
                                if translates[1] == new_language:
                                    for new_names_languages in PROGRAMS[language]["initials"]:
                                        if translates[0].count(new_names_languages) == 0:
                                            translates[0].append(new_names_languages)
                                else:
                                    PROGRAMS[language]["translated"].append([PROGRAMS[language]["initials"], new_language])

            # Verificar si se puede generar nuevos interpretados mediantes los nuevos traductores y maquinas.
            interpreters_languages = INTERPRETERS.copy().keys()
            for base_language in interpreters_languages:
                if TRANSLATORS[machine].get(base_language) is not None:
                    for new_language in TRANSLATORS[machine][base_language]:
                        if new_language not in INTERPRETERS:
                            INTERPRETERS.update({new_language: INTERPRETERS[base_language]})
                        else:
                            for interpreters_origin in INTERPRETERS[new_language]:
                                if INTERPRETERS[new_language].count(interpreters_origin) == 0:
                                    INTERPRETERS[new_language].append(interpreters_origin)
    MACHINES.remove(LOCAL)

# Procedimiento que permite verificar si un programada dado es ejecutable.
# Realizando una busqueda de los lenguajes principales definidos para dicho programa
# se toma el primero y se verifica. En caso contrario es porque no esta definido.
def EXECUTING(name_of_program): 
    main_language = ""
    for languages in PROGRAMS.keys():
        if name_of_program in PROGRAMS[languages]["initials"]:
            main_language = languages
            break
    
    # Verificamos existencia del programa.
    if main_language == "":
        print(f"*  El archivo '{name_of_program}' no ha sido definido.")
        return
    
    # En caso de temer una maquina.
    elif main_language in MACHINES or main_language == LOCAL:
        print(f"*  Si, es posible ejecutar '{name_of_program}' en {main_language}")
        return
    
    # De lo contrario verificamos si podemos llegar mediante las traducciones del programa.
    else:
        MACHINES.insert(0, LOCAL)
        for machine in MACHINES:
            for programs in PROGRAMS.keys():
                if "translated" in PROGRAMS[programs]:
                    for program_language in PROGRAMS[programs]["translated"]:
                        if machine == program_language[1] and name_of_program in program_language[0]:
                            if machine == LOCAL:
                                    print(f"*  Si, es posible ejecutar el programa '{name_of_program}' En {main_language}")
                                    return

                            for transtales_language in TRANSLATORS.keys():
                                if (TRANSLATORS[transtales_language].get(programs) is not None and 
                                    program_language[1] in TRANSLATORS[transtales_language][programs] and 
                                    transtales_language in MACHINES):
                                    print(f"*  Si, es posible ejecutar el programa '{name_of_program}' En {main_language}")
                                    return

                            if TRANSLATORS.get(machine) is not None:
                                if TRANSLATORS[machine].get(programs) is not None and main_language in TRANSLATORS[machine][programs]:  
                                    print(f"*  Si, es posible ejecutar el programa '{name_of_program}' En {main_language}")
                                    return
        MACHINES.remove(LOCAL)
        print(f"*  No es posible ejecutar el programa '{name_of_program}'.")

# Procedimiento que permite verificar si dado una lenguaje descrito en una maquina ver si otros podemos formar
# otros traductores.
def NEW_TRANSLATOR(base_language):
    if base_language in MACHINES:
        base_language_list = TRANSLATORS[base_language].copy().keys()
        for origins in base_language_list:
            if origins in TRANSLATORS:
                for destinations in TRANSLATORS[base_language][origins]:
                    if destinations not in TRANSLATORS:
                        TRANSLATORS.update({destinations : TRANSLATORS[origins]})
                    else:
                        for new_origins in TRANSLATORS[origins].keys():
                            if new_origins not in TRANSLATORS[destinations]:
                                TRANSLATORS[destinations].update(TRANSLATORS[origins])
                            else:
                                for new_destinations in TRANSLATORS[destinations][new_origins]:
                                    if TRANSLATORS[destinations][new_origins].count(new_destinations) == 0:
                                        TRANSLATORS[destinations][new_origins].append(new_destinations)
                                    
# Procedimiento que permite realizar una revision de nuevos interpretes y traductores.
# Se van a gregando aquellos nuevos traductores creados en base a maquinas e/o interpretres.
def IN_MACHINE_UPDATE(base_language):
    for machine in MACHINES:
        if TRANSLATORS.get(machine) is not None and base_language in TRANSLATORS[machine]:
            # Revisemos para los traductores
            for origin in TRANSLATORS[base_language].keys():
                if origin not in TRANSLATORS[machine]:
                    TRANSLATORS[machine].update(TRANSLATORS[base_language])
                else:
                    TRANSLATORS[machine][origin].extend(TRANSLATORS[base_language][origin])

            # Revisemos para los interpretadores.
            for origin in TRANSLATORS[machine][base_language]:
                if origin not in INTERPRETERS:
                    INTERPRETERS.update({ origin : INTERPRETERS[base_language] })
                else:
                    for interpreters_origin in INTERPRETERS[origin]:
                        if INTERPRETERS[origin].count(interpreters_origin) == 0:
                            INTERPRETERS[origin].append(interpreters_origin)
  
# Procedimiento que permite realizar la inclusion de nuevos traductores.
# Estos seran agregados al diccionario respectivo, cuya primera key esta delimitada por
# lenguaje en que esta escrito, luego como segunda key el lenguaje origen y finalmente una lista de los
# lenguajes destino que posee.
def ADD_TRANSTALOR(base_language, origin_language, destination_language):
    if base_language in TRANSLATORS:
        if origin_language in TRANSLATORS[base_language]:
            TRANSLATORS[base_language].get(origin_language).append(destination_language)
        else:
            TRANSLATORS[base_language].update({origin_language : [destination_language]})    
    else:
        TRANSLATORS.update({base_language : dict([(origin_language, [destination_language])])})
    
    # Buscamos nuevas maquinas y nuevos traductores.
    NEW_TRANSLATOR(base_language)
    IN_MACHINE_UPDATE(base_language)
    GLOBAL_UPDATE()

    print(f"*  Se definio un traductor de {origin_language} hacia {destination_language}, escrito en {base_language}")

# Procedimiento que permite realizar la inclusion de nuevos programas dados por consola.
# En este casos son almacenados en un diccionario cuyo primer key esta delimitado por el 
# lenguaje en que esta escrito, luego una key en en caso de ser de tipo "initials" indicando
# que es el origen de entrada y otro key "translated" que sera mediante un procesamiento en 
# caso de poder ser traducido a otro lenguaje.
def ADD_PROGRAM(name_of_program, language_of_program):
    if language_of_program in PROGRAMS:
        if name_of_program in PROGRAMS[language_of_program]["initials"]:
            print("*      -> ERROR 403 <-                                                       *")
            print(f"*        El programa {name_of_program} ya fue escrito en {language_of_program}")
        else:
            PROGRAMS[language_of_program]["initials"].append(name_of_program)
    else:
        PROGRAMS.update({language_of_program : {"initials" : [name_of_program]}})
    
    # Realizando una actualizacion para el programa dado particularmente.
    for machine in MACHINES:
        if TRANSLATORS.get(machine) is not None and language_of_program in TRANSLATORS[machine]:
            for newLan in TRANSLATORS[machine][language_of_program]:
                if "translated" not in PROGRAMS[language_of_program]:
                    PROGRAMS[language_of_program].update({"translated" : [[[name_of_program], newLan]]})
                else:
                    for traduc in PROGRAMS[language_of_program]["translated"]:
                        if traduc[1] == newLan:
                            if traduc[0].count(name_of_program) == 0:
                                traduc[0].append(name_of_program)
                        else:
                            PROGRAMS[language_of_program]["translated"].append([[name_of_program], newLan])
    
    # En caso de que hayan traducciones se realiza una nueva actualizacion.          
    if PROGRAMS[language_of_program].get("translated") is not None:
        MACHINES.insert(0, LOCAL)
        update_programs = PROGRAMS[language_of_program]["translated"]
        for program in update_programs:
            for machine in MACHINES:
                if machine in TRANSLATORS and TRANSLATORS[machine].get(program[1]) is not None:
                    for tranlations in TRANSLATORS[machine][program[1]]:
                        if tranlations != program[1]:
                            PROGRAMS[language_of_program]["translated"].append([ program[0] , tranlations ])
        MACHINES.remove(LOCAL)

    print(f"*  Se definio el programa '{name_of_program}', ejecutable en {language_of_program}")

# Procedimiento que permite realizar la inclusion de nuevos interpreteradores.
# Estos seran agregados al diccionario respectivo, cuya primera key esta delimitada por
# lenguaje en que esta escrito que almacena una lista de los lenguaje objetivo del interpretre.
def ADD_INTERPRETER(base_language, bridge_language):
    if base_language in INTERPRETERS:
        INTERPRETERS[base_language].append(bridge_language)
    else:
        INTERPRETERS.update({base_language : [bridge_language]})
    
    if base_language.upper() == LOCAL or base_language in MACHINES:
        MACHINES.append(bridge_language)

    # Buscamos nuevas maquinas y nuevos interpretadores.
    NEW_TRANSLATOR(base_language)
    IN_MACHINE_UPDATE(base_language)
    GLOBAL_UPDATE()

    print(f"*  Se definio un interprete para {bridge_language}, escrito en {base_language}")