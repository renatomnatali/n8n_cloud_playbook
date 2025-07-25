# n8n Cloud Playbook

Este repositório contém o **Playbook operacional para n8n Cloud**. Ele foi pensado para ajudar assistentes de IA a gerar arquivos JSON de workflows prontos para serem importados no n8n Cloud com o mínimo de erros possíveis.

Os arquivos `n8n_cloud_playbook_v*.yaml` trazem um conjunto de padrões, checklists e dicas práticas em português. Eles abordam pontos como ordenação de importação, compatibilidade de nodes, boas práticas de exportação e um passo a passo de revisão antes de ativar cada fluxo.

## Como utilizar

1. Escolha o arquivo YAML da versão mais recente (ex.: `n8n_cloud_playbook_v13.yaml`).
2. Consulte as seções do playbook para orientar a criação ou correção dos seus workflows.
3. Gere o JSON do fluxo no n8n seguindo as recomendações de nomenclatura, nós compatíveis e políticas de segurança presentes no playbook.
4. Importe os fluxos no n8n Cloud respeitando a ordem sugerida (sub‑workflows, fluxos autônomos e por último o orquestrador).
5. Ao iniciar uma conversa com o assistente, anexe o playbook escolhido e deixe claro que ele deve segui‑lo ao gerar os arquivos JSON. Em seguida, forneça o prompt com a automação desejada.

Modificações em qualquer arquivo `n8n_cloud_playbook_v*.yaml` fazem a ação do GitHub criar automaticamente uma nova versão numerada. Por isso, sempre utilize o arquivo de maior versão.

## Contribuindo

Pull requests são bem‑vindos. Caso queira propor melhorias ou correções, abra uma issue ou PR explicando a motivação da mudança. A geração de novas versões do playbook é automatizada pela ação `bump-playbook-version.yml`.

## Licença

Distribuído sob a [GNU GPL v3](LICENSE).

