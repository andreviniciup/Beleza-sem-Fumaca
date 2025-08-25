from app import app, db, Questao

def insert_real_questions():
    with app.app_context():
        # Limpar questões existentes
        Questao.query.delete()
        db.session.commit()
        
        # Lista das 50 questões reais
        questoes = [
            {
                'pergunta': 'Como o tabagismo afeta a saúde da pele?',
                'opcao_a': 'Aumenta a elasticidade e o colágeno.',
                'opcao_b': 'Pode causar envelhecimento precoce e rugas.',
                'opcao_c': 'Melhora a hidratação e o brilho natural.',
                'opcao_d': 'Previne o aparecimento de manchas.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Qual é o efeito do tabagismo nos dentes?',
                'opcao_a': 'Ajuda a manter os dentes mais brancos.',
                'opcao_b': 'Fortalece o esmalte dentário.',
                'opcao_c': 'Pode causar manchas, mau hálito e doenças na gengiva.',
                'opcao_d': 'Diminui o risco de cáries.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'O tabagismo pode causar quais problemas no cabelo?',
                'opcao_a': 'Cabelo mais brilhante e forte.',
                'opcao_b': 'Acelera o crescimento do cabelo.',
                'opcao_c': 'Previne o aparecimento de cabelos brancos.',
                'opcao_d': 'Queda de cabelo e enfraquecimento dos fios.',
                'resposta_correta': 'D'
            },
            {
                'pergunta': 'Qual das alternativas é verdadeira sobre o tabagismo e a aparência geral?',
                'opcao_a': 'Melhora a saúde da pele e dos cabelos.',
                'opcao_b': 'Não tem impacto significativo na aparência.',
                'opcao_c': 'Pode causar rugas, pele opaca e queda de cabelo.',
                'opcao_d': 'Contribui para um aspecto mais jovem.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Fumar aumenta o risco de quais problemas respiratórios que afetam o bem-estar?',
                'opcao_a': 'Asma e Doença Pulmonar Obstrutiva Crônica (DPOC).',
                'opcao_b': 'Melhora da capacidade pulmonar.',
                'opcao_c': 'Redução do risco de pneumonia.',
                'opcao_d': 'Limpeza das vias aéreas.',
                'resposta_correta': 'A'
            },
            {
                'pergunta': 'O que o tabagismo faz com o aspecto dos dentes a longo prazo?',
                'opcao_a': 'Os dentes ficam mais brancos com o tempo.',
                'opcao_b': 'Pode causar mau hálito crônico e manchas persistentes.',
                'opcao_c': 'Torna os dentes mais fortes e resistentes.',
                'opcao_d': 'Estimula a produção de saliva protetora.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Fumar pode afetar o humor e o bem-estar emocional de qual forma?',
                'opcao_a': 'Funciona como um antidepressivo eficaz a longo prazo.',
                'opcao_b': 'Diminui permanentemente os níveis de estresse.',
                'opcao_c': 'Pode aumentar os níveis de ansiedade e irritabilidade.',
                'opcao_d': 'Reduz a fadiga e aumenta a disposição geral.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Qual é o efeito do tabagismo na circulação sanguínea?',
                'opcao_a': 'Melhora a circulação e oxigenação dos tecidos.',
                'opcao_b': 'Aumenta a espessura do sangue, facilitando o fluxo.',
                'opcao_c': 'Não tem efeito sobre o sistema circulatório.',
                'opcao_d': 'Pode diminuir o fluxo sanguíneo para órgãos e pele.',
                'resposta_correta': 'D'
            },
            {
                'pergunta': 'O tabagismo pode contribuir para qual condição relacionada à saúde ocular?',
                'opcao_a': 'Melhora da visão noturna.',
                'opcao_b': 'Catarata e degeneração macular.',
                'opcao_c': 'Maior proteção contra a luz ultravioleta.',
                'opcao_d': 'Redução da pressão intraocular.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Fumar está relacionado ao aumento de quais tipos de rugas?',
                'opcao_a': 'Rugas apenas nas mãos e nos pés.',
                'opcao_b': 'Redução geral das rugas faciais.',
                'opcao_c': 'Rugas finas e profundas, especialmente ao redor da boca e dos olhos.',
                'opcao_d': 'Rugas causadas exclusivamente pela exposição solar.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Qual substância do cigarro é a principal responsável pela dependência química?',
                'opcao_a': 'Alcatrão',
                'opcao_b': 'Monóxido de Carbono',
                'opcao_c': 'Nicotina',
                'opcao_d': 'Amônia',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'O tabagismo é um fator de risco para qual tipo de câncer, além do de pulmão?',
                'opcao_a': 'Câncer de pele não melanoma.',
                'opcao_b': 'Apenas câncer de pulmão.',
                'opcao_c': 'Câncer de bexiga, boca, laringe e esôfago.',
                'opcao_d': 'Não há evidências que liguem o fumo a outros cânceres.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Como o monóxido de carbono, presente na fumaça do cigarro, afeta o corpo?',
                'opcao_a': 'Melhora a capacidade do sangue de transportar oxigênio.',
                'opcao_b': 'Reduz a capacidade do sangue de transportar oxigênio.',
                'opcao_c': 'Fortalece os músculos do coração.',
                'opcao_d': 'Ajuda a limpar os pulmões.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Qual o impacto do tabagismo na saúde dos ossos?',
                'opcao_a': 'Aumenta a densidade óssea.',
                'opcao_b': 'Não afeta a saúde óssea.',
                'opcao_c': 'Reduz o risco de fraturas.',
                'opcao_d': 'Aumenta o risco de osteoporose.',
                'resposta_correta': 'D'
            },
            {
                'pergunta': 'O que é o "tabagismo passivo"?',
                'opcao_a': 'Fumar cigarros com baixo teor de nicotina.',
                'opcao_b': 'A inalação involuntária da fumaça do cigarro de outras pessoas.',
                'opcao_c': 'O ato de fumar apenas em ambientes abertos.',
                'opcao_d': 'Fumar cigarros eletrônicos.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Qual o efeito do tabagismo na cicatrização de feridas?',
                'opcao_a': 'Acelera o processo de cicatrização.',
                'opcao_b': 'Não interfere na recuperação de lesões.',
                'opcao_c': 'Retarda a cicatrização e aumenta o risco de infecções.',
                'opcao_d': 'Fortalece a pele, tornando-a mais resistente a cortes.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'O tabagismo afeta a fertilidade feminina de que maneira?',
                'opcao_a': 'Aumenta as chances de concepção.',
                'opcao_b': 'Pode dificultar a gravidez e antecipar a menopausa.',
                'opcao_c': 'Melhora a qualidade dos óvulos.',
                'opcao_d': 'Não tem impacto na saúde reprodutiva da mulher.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Qual doença cardiovascular tem seu risco significativamente aumentado pelo tabagismo?',
                'opcao_a': 'Insuficiência venosa.',
                'opcao_b': 'Pressão baixa (hipotensão).',
                'opcao_c': 'Infarto do miocárdio e acidente vascular cerebral (AVC).',
                'opcao_d': 'Bradicardia (ritmo cardíaco lento).',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Parar de fumar traz benefícios para a saúde em quanto tempo?',
                'opcao_a': 'Apenas após 20 anos sem fumar.',
                'opcao_b': 'Os benefícios começam a ser percebidos minutos após o último cigarro.',
                'opcao_c': 'Somente se a pessoa fumou por menos de 5 anos.',
                'opcao_d': 'Não há benefícios significativos após anos de tabagismo.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Como o tabagismo afeta o paladar e o olfato?',
                'opcao_a': 'Melhora e apura ambos os sentidos.',
                'opcao_b': 'Não causa alterações no paladar ou olfato.',
                'opcao_c': 'Pode diminuir a capacidade de sentir cheiros e gostos.',
                'opcao_d': 'Aumenta a sensibilidade apenas a sabores doces.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Qual o nome da doença pulmonar crônica mais comum causada pelo tabagismo?',
                'opcao_a': 'Asma alérgica.',
                'opcao_b': 'Tuberculose.',
                'opcao_c': 'Fibrose cística.',
                'opcao_d': 'DPOC (Doença Pulmonar Obstrutiva Crônica).',
                'resposta_correta': 'D'
            },
            {
                'pergunta': 'O uso de cigarros eletrônicos ("vapes") é considerado seguro?',
                'opcao_a': 'Sim, são totalmente inofensivos à saúde.',
                'opcao_b': 'Não, eles contêm substâncias tóxicas e nicotina, oferecendo riscos à saúde.',
                'opcao_c': 'São mais perigosos que cigarros convencionais.',
                'opcao_d': 'A segurança é garantida para todos os usuários.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'O que acontece com a pressão arterial de um fumante imediatamente após fumar um cigarro?',
                'opcao_a': 'Diminui drasticamente.',
                'opcao_b': 'Permanece inalterada.',
                'opcao_c': 'Aumenta temporariamente.',
                'opcao_d': 'Torna-se mais estável.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'O tabagismo pode interferir no desempenho atlético?',
                'opcao_a': 'Sim, pois reduz a capacidade pulmonar e o transporte de oxigênio.',
                'opcao_b': 'Não, muitos atletas de elite são fumantes.',
                'opcao_c': 'Apenas em esportes de alta intensidade.',
                'opcao_d': 'Melhora a resistência por estimular o sistema nervoso.',
                'resposta_correta': 'A'
            },
            {
                'pergunta': 'Crianças expostas ao fumo passivo têm maior risco de desenvolver qual condição?',
                'opcao_a': 'Diabetes tipo 1.',
                'opcao_b': 'Obesidade infantil.',
                'opcao_c': 'Infecções de ouvido, asma e bronquite.',
                'opcao_d': 'Miopia.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Qual o efeito do tabagismo na saúde do sistema digestivo?',
                'opcao_a': 'Melhora a digestão e previne a azia.',
                'opcao_b': 'Aumenta o risco de úlceras e câncer de estômago.',
                'opcao_c': 'Não tem relação com problemas digestivos.',
                'opcao_d': 'Fortalece a mucosa do estômago.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Por que os fumantes frequentemente têm os dedos e unhas amarelados?',
                'opcao_a': 'É um efeito da má circulação sanguínea.',
                'opcao_b': 'É causado pelo depósito de alcatrão e nicotina.',
                'opcao_c': 'É um sinal de excesso de vitaminas no corpo.',
                'opcao_d': 'É uma reação alérgica ao papel do cigarro.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'O que é a "tosse do fumante"?',
                'opcao_a': 'Um sinal de que os pulmões estão se limpando eficientemente.',
                'opcao_b': 'Uma tosse crônica causada pela irritação das vias aéreas.',
                'opcao_c': 'Uma condição rara que afeta apenas fumantes iniciantes.',
                'opcao_d': 'Um sintoma de melhora da função pulmonar.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Fumar durante a gravidez está associado a que risco para o feto?',
                'opcao_a': 'Aceleração do desenvolvimento cerebral.',
                'opcao_b': 'Aumento do peso ao nascer.',
                'opcao_c': 'Restrição de crescimento e baixo peso ao nascer.',
                'opcao_d': 'Menor chance de complicações no parto.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Como o sistema imunológico é afetado pelo tabagismo?',
                'opcao_a': 'Torna-se mais forte e responsivo.',
                'opcao_b': 'Fica enfraquecido, aumentando a suscetibilidade a infecções.',
                'opcao_c': 'Não sofre alterações significativas.',
                'opcao_d': 'Melhora a capacidade de combater células cancerígenas.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Qual o risco de desenvolver diabetes tipo 2 para fumantes?',
                'opcao_a': 'É menor do que em não fumantes.',
                'opcao_b': 'É o mesmo que em não fumantes.',
                'opcao_c': 'É significativamente maior do que em não fumantes.',
                'opcao_d': 'O tabagismo previne o desenvolvimento de diabetes.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'O que o alcatrão, presente no cigarro, faz nos pulmões?',
                'opcao_a': 'Ajuda a lubrificar as vias aéreas.',
                'opcao_b': 'É uma substância inofensiva que é expelida totalmente.',
                'opcao_c': 'Cobre os pulmões, danificando os cílios e causando câncer.',
                'opcao_d': 'Fortalece os alvéolos pulmonares.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'O tabagismo pode causar problemas de audição?',
                'opcao_a': 'Não, a audição não é afetada pelo fumo.',
                'opcao_b': 'Sim, pode aumentar o risco de perda auditiva.',
                'opcao_c': 'Melhora a sensibilidade auditiva.',
                'opcao_d': 'Apenas em fumantes de cachimbo.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Após parar de fumar, o risco de ter um infarto:',
                'opcao_a': 'Aumenta nos primeiros anos.',
                'opcao_b': 'Nunca retorna ao nível de um não fumante.',
                'opcao_c': 'Começa a diminuir significativamente já no primeiro ano.',
                'opcao_d': 'Permanece o mesmo de quando a pessoa fumava.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'O tabagismo afeta a saúde bucal apenas nos dentes?',
                'opcao_a': 'Sim, os efeitos se limitam ao amarelamento dos dentes.',
                'opcao_b': 'Não, também aumenta o risco de câncer de boca e doenças na gengiva.',
                'opcao_c': 'Sim, e apenas de forma estética.',
                'opcao_d': 'Não, mas os outros problemas são extremamente raros.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Como o tabagismo pode levar à disfunção erétil nos homens?',
                'opcao_a': 'Aumentando os níveis de testosterona.',
                'opcao_b': 'Melhorando o humor e a libido.',
                'opcao_c': 'Prejudicando o fluxo sanguíneo para o pênis.',
                'opcao_d': 'O tabagismo não tem relação com a disfunção erétil.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Qual a relação entre tabagismo e o sono?',
                'opcao_a': 'Melhora a qualidade do sono profundo.',
                'opcao_b': 'Pode causar insônia e fragmentar o sono.',
                'opcao_c': 'Não tem efeito sobre os padrões de sono.',
                'opcao_d': 'Ajuda a regular o ciclo circadiano.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Animais de estimação em casas de fumantes estão em risco?',
                'opcao_a': 'Não, a fumaça não afeta os animais.',
                'opcao_b': 'Sim, eles podem desenvolver problemas respiratórios e câncer.',
                'opcao_c': 'Apenas se eles ingerirem o cigarro.',
                'opcao_d': 'Sim, mas apenas animais de pequeno porte.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'O que é a "fumaça de terceira mão"?',
                'opcao_a': 'A fumaça que sai da ponta do cigarro.',
                'opcao_b': 'A fumaça exalada pelo fumante.',
                'opcao_c': 'Os resíduos tóxicos da fumaça que se depositam em superfícies.',
                'opcao_d': 'Um tipo de cigarro eletrônico.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Por que parar de fumar pode levar ao ganho de peso temporário?',
                'opcao_a': 'Porque o corpo passa a absorver mais gordura.',
                'opcao_b': 'A nicotina acelera o metabolismo e suprime o apetite.',
                'opcao_c': 'É um mito, a maioria das pessoas perde peso.',
                'opcao_d': 'Porque a comida fica menos saborosa.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'O tabagismo aumenta o risco de desenvolver qual doença autoimune?',
                'opcao_a': 'Lúpus.',
                'opcao_b': 'Artrite reumatoide.',
                'opcao_c': 'Vitiligo.',
                'opcao_d': 'Esclerose múltipla.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Qual o efeito do cigarro no envelhecimento cerebral?',
                'opcao_a': 'Protege o cérebro contra o envelhecimento.',
                'opcao_b': 'Não tem impacto no cérebro.',
                'opcao_c': 'Pode acelerar o declínio cognitivo e aumentar o risco de demência.',
                'opcao_d': 'Melhora a memória de longo prazo.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'O filtro do cigarro consegue reter todas as substâncias tóxicas?',
                'opcao_a': 'Sim, o filtro torna o cigarro seguro.',
                'opcao_b': 'Sim, retém 100% das toxinas.',
                'opcao_c': 'Não, ele retém apenas uma pequena parte das partículas maiores.',
                'opcao_d': 'O filtro serve apenas para segurar o tabaco.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Parar de fumar melhora a aparência da pele?',
                'opcao_a': 'Não, os danos causados são permanentes e irreversíveis.',
                'opcao_b': 'Sim, a circulação melhora, o que pode restaurar um pouco da cor e vitalidade.',
                'opcao_c': 'A pele piora após parar de fumar.',
                'opcao_d': 'Apenas se a pessoa usar cremes específicos.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'O tabagismo pode afetar a voz de uma pessoa?',
                'opcao_a': 'Sim, pode deixar a voz mais grossa e rouca.',
                'opcao_b': 'Não, a voz não é alterada.',
                'opcao_c': 'Sim, tende a deixar a voz mais aguda.',
                'opcao_d': 'Apenas em cantores profissionais.',
                'resposta_correta': 'A'
            },
            {
                'pergunta': 'Qual a porcentagem aproximada de mortes por câncer de pulmão atribuídas ao tabagismo?',
                'opcao_a': 'Cerca de 20%',
                'opcao_b': 'Cerca de 50%',
                'opcao_c': 'Cerca de 90%',
                'opcao_d': 'Menos de 10%',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'O que são os sintomas da abstinência de nicotina?',
                'opcao_a': 'Sensação de euforia e energia.',
                'opcao_b': 'Aumento da capacidade de concentração.',
                'opcao_c': 'Irritabilidade, ansiedade, desejo intenso de fumar.',
                'opcao_d': 'Melhora do humor e do sono.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Fumar cigarros mentolados é mais seguro que os normais?',
                'opcao_a': 'Sim, o mentol protege os pulmões.',
                'opcao_b': 'Não, eles podem ser mais perigosos por facilitar a inalação mais profunda.',
                'opcao_c': 'São iguais aos cigarros normais.',
                'opcao_d': 'São recomendados para quem quer parar de fumar.',
                'resposta_correta': 'B'
            },
            {
                'pergunta': 'Como o tabagismo afeta o tratamento de outras doenças, como o câncer?',
                'opcao_a': 'Ajuda na eficácia dos tratamentos.',
                'opcao_b': 'Não interfere nos tratamentos.',
                'opcao_c': 'Pode reduzir a eficácia da quimioterapia e radioterapia.',
                'opcao_d': 'Acelera a recuperação pós-tratamento.',
                'resposta_correta': 'C'
            },
            {
                'pergunta': 'Após 15 anos sem fumar, o risco de doença coronariana de um ex-fumante é:',
                'opcao_a': 'Maior do que quando fumava.',
                'opcao_b': 'O mesmo de quando fumava.',
                'opcao_c': 'Ligeiramente menor, mas ainda muito alto.',
                'opcao_d': 'Semelhante ao de uma pessoa que nunca fumou.',
                'resposta_correta': 'D'
            }
        ]
        
        # Inserir questões
        for questao_data in questoes:
            questao = Questao(**questao_data)
            db.session.add(questao)
        
        db.session.commit()
        print(f"✅ {len(questoes)} questões inseridas com sucesso!")

if __name__ == "__main__":
    insert_real_questions()
