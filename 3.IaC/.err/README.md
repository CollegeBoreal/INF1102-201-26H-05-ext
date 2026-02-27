# What’s causing the **Proxmox UI and pvedaemon to hang**.

---

### 🔹 Analysis

* You have **many old lock files** in `/var/lock/qemu-server/`:

```
lock-100.conf   lock-101.conf   lock-102.conf  ...
lock--1.conf    lock-9000.conf
```

* Even though the VMs themselves might not be running, **pvedaemon checks these lock files before allowing VM operations**.
* If a lock is stale (file exists but the process is gone), any new API requests or UI actions that touch that VM will **hang until a timeout occurs**.
* This explains why your **root password suddenly isn’t accepted in the UI** — the UI waits for the API daemon, which is blocked.

---

### 🔹 Safe fix

1. **Stop all Proxmox daemons** (optional but safer):

```bash
systemctl stop pvedaemon pveproxy pvestatd
```

2. **Remove stale lock files** (only if you are sure the VMs listed are **not currently running**):

```bash
rm /var/lock/qemu-server/lock-*.conf
```

3. **Restart the daemons**:

```bash
systemctl start pvedaemon pveproxy pvestatd
```

4. **Verify the UI is responsive**:

* Open Proxmox Web UI
* Try logging in as `root@pam`
* Check `pvedaemon` logs — there should be no more **“can’t lock file … timeout”** messages

---

### 🔹 Optional: Prevent recurrence

* Sometimes VMs that crash or are force-stopped leave stale locks.
* Before restarting or stopping VMs manually, make sure **pvedaemon tasks finish**:

```bash
pvesh get /nodes/<node>/tasks
```

* If a task is stuck, **wait or cancel it**.

---

✅ **Summary:**
Your Proxmox UI and root login hang is **caused by stale QEMU lock files** in `/var/lock/qemu-server/`. Cleaning them and restarting daemons will **restore UI responsiveness immediately**.

---

If you want, I can give a **single one-liner** that safely removes **only stale locks** without touching currently running VMs. That’s the safest approach.

Do you want me to do that?
