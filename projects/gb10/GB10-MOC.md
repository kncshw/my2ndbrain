# GB10 Project — Map of Content

Deploying Nemotron-3-Super-120B (NVFP4) on Dell Pro Max GB10 (Blackwell B10) for security/pentest inference + LoRA fine-tuning.

## Status
- Phase 1 (L4 mock): **Complete** → [[Mock_L4]]
- Phase 2-6 (GB10 hardware): **Done, except LoRA fine-tuning and RAG**

## Documents

### Planning
- [[Gb10_QA]] — requirements Q&A (2026-03-26), all key decisions recorded here
- [[GB10_plan]] — master 6-phase execution roadmap

### Technical Reference
- [[LORA_and_RAG_highlevel_design]] — LoRA mechanics, RAG architecture, dataset formats, eval methodology
- [[HTTPS_Reverse_Proxy]] — nginx/Caddy HTTPS setup with IP-based access control for production

### Execution Reports
- [[Mock_L4]] — Phase 1 validation on L4 x86_64; scripts reusable on GB10
- [[Gemma4_Deployment]] — day-one Gemma-4-26B deployment case study; lessons on container isolation

## Key Decisions
| Decision | Choice |
|---|---|
| Primary model | Nemotron-3-Super-120B NVFP4 |
| Serving framework | vLLM via Docker (eugr/spark-vllm-docker) |
| Fine-tuning | LoRA (HuggingFace PEFT) |
| Domain | Security operations + red team |
| Proxy | Caddy (preferred) or nginx |

## Next Actions
- [ ] GB10 hardware arrives → execute Phase 2 ([[GB10_plan]])
- [ ] Build tool-call dataset → [[LORA_and_RAG_highlevel_design]]
- [ ] Scaffold RAG pipeline with CVE/cheatsheet data
- [ ] Deploy HTTPS proxy → [[HTTPS_Reverse_Proxy]]
